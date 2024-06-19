from allauth.account.views import LogoutView
from users.forms import RegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView, ListView
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


class ProfileView(ListView):
    template_name = 'users/profile.html'
    model = Profile
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all()


class CustomLogoutView(LogoutView):
    next_page = 'home'
    template_name = 'users/logout.html'  # путь к вашему шаблону
