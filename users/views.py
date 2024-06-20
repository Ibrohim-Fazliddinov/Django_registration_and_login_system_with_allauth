from allauth.account.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from users.forms import RegistrationForm, LoginForm, UpdateProfileForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView

from users.models import Profile


class HomeView(TemplateView):
    template_name = 'users/home.html'


class RegisterView(View):
    form = RegistrationForm()
    initial = {'key': 'value'}
    template_name = 'users/register.html'
    extra_context = {'title': 'Register'}

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # если пользователь уже был уже залогинен, он перенаправляется на домашнюю страницу
            return redirect('home')
        # если пользователь не был залогинен, вызывается метод dispatch для передачи запроса далее для обработки
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(initial=self.initial)
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)

        # если форма валидна, пользователь регистрируется и входит
        if form.is_valid():
            form.save()  # = user
            # Аутентификация пользователя
            # login(request, user)
            username = form.cleaned_data.get('nickname')
            messages.success(request, f'{username} your account has been created!')

            return redirect('login')  # Перенаправляем на домашнюю страницу
        # в ином случае, ошибка
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ProfileView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not logged in!')
            return redirect('login')
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return redirect('profile_not_found')  # Или другой подходящий обработчик

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.get_object().pk  # Правильно добавляем pk в контекст
        return context


class CustomLogoutView(LogoutView):
    next_page = 'home'
    template_name = 'users/logout.html'  # путь к вашему шаблону


class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'users/update_profile.html'
    fields = ['user', 'bio', 'user_photo']
    context_object_name = 'profile'
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not logged in!')
            return redirect('login')
        return super(UpdateProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        # Ensure the correct profile instance is fetched
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['user_form'] = UserUpdateForm(self.request.POST,
                                                  instance=self.request.user)
            context['profile_form'] = UpdateProfileForm(self.request.POST, self.request.FILES,
                                                        instance=self.request.user.profile)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
            context['profile_form'] = UpdateProfileForm(instance=self.request.user.profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            return self.form_invalid(user_form, profile_form)

    def form_invalid(self, user_form, profile_form):
        context = self.get_context_data()
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return self.render_to_response(context)
