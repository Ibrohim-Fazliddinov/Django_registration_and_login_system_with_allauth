from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView
from allauth.account.views import LogoutView
from django.urls import reverse_lazy

from users.forms import (
    RegistrationForm,
    LoginForm,
    UpdateProfileForm,
    UserUpdateForm
)

from django.views.generic import (
    View,
    TemplateView,
    UpdateView,
    DetailView
)


class HomeView(TemplateView):
    template_name = 'users/home.html'  # Главная страница


class ProfileView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/profile.html'  # Страница профиля

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not logged in!')
            return redirect('login')  # Перенаправление на страницу входа, если пользователь не аутентифицирован
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            messages.error(self.request, 'Profile not found.')
            return redirect('home')  # Перенаправление на домашнюю страницу, если профиль не найден

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.get_object().pk  # Добавление pk в контекст
        return context


class RegisterView(View):
    form = RegistrationForm()
    initial = {'key': 'value'}
    template_name = 'users/register.html'
    extra_context = {'title': 'Register'}  # Страница регистрации

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Перенаправление на домашнюю страницу, если пользователь аутентифицирован
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')  # Перенаправление на страницу входа
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'  # Страница входа

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)  # Сессия будет закрыта при закрытии браузера
            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)


class CustomLogoutView(LogoutView):
    next_page = 'home'  # Страница после выхода
    template_name = 'users/logout.html'  # Шаблон для выхода


class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'users/update_profile.html'  # Страница обновления профиля
    fields = ['user', 'bio', 'user_photo']
    context_object_name = 'profile'
    success_url = reverse_lazy('profile')  # Перенаправление на страницу профиля после успешного обновления

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not logged in!')
            return redirect('login')  # Перенаправление на страницу входа, если пользователь не аутентифицирован
        return super(UpdateProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user.profile  # Получение профиля текущего пользователя

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
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


class ChangePasswordView(PasswordChangeView):
    template_name = 'users/change_password.html'  # Страница изменения пароля
    success_url = reverse_lazy('home')  # Перенаправление на домашнюю страницу после успешного изменения пароля
