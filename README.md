EN-version
# Project Goal:

- This project aims to deepen my understanding of Django and enhance or acquire new programming skills.
- Additionally, it will serve as a template for developing an authentication system for applications.
- This project can be easily integrated into larger applications (though there are minor challenges with email distribution and third-party authentication APIs).

# System Description:

- User Authentication and Authorization.
- User Profile.

## User Authentication and Authorization:

- Core Features:
    - **Registration:** Users can register on the site.
    - **Login:** Registered users can log in to the site using their username (login) and password.
    - **Social Login:** Users can log in to the site through their Google, GitHub, or Spotify accounts.
    - **Password Reset:** Users can change their password or reset it via email if they forget it.

## User Profile:

- Core Features:
    - **Profile:** Authenticated users can access their profile.
    - **Profile Editing:** Users can edit their profile, including their profile picture, name, and bio section.

# Technology Stack:

- Python 3.12
- Django 5
- Bootstrap 5


## Useful Links or Sources of Inspiration:

- [Reset Password](https://www.youtube.com/watch?v=sFPcd6myZrY&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=21)
- [Login and register with Django](https://github.com/earthcomfy/Django-registration-and-login-system)

![Снимок экрана 2024-06-22 в 19.11.53.png](..%2F..%2FDesktop%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-22%20%D0%B2%2019.11.53.png)

RU-version

# **1. Цель Проекта:**

- Это проект, который поможет мне поглубже погрузится в Джанго и улучшить или же освоить новые навыки программирования.
- А так же это будет моим шаблоном для написание системы аутентификации для приложений.
- Этот проект может быть легко интегрирован в другие большие приложения.(есть небольшие сложности для рассылки по почте и много гемора с 3-ти сторонней аутентификации в плане того что нужно API приложений)

# 2.  **Описание Системы:**

- Аутентификация и Авторизация пользователя.
- Профиль пользователя.

## 2.1 Аутентификация и Авторизация пользователя:

- Основные функции:
    - Регистрация: Пользователь может регистрироваться на сайте.
    - Логин: Зарегистрированный пользователь может зайти в сайт, используя свой username(login) и пароль.
    - Вход через социальные-приложения: Вы сможете входить(залогиниться) в сайт через свои аккаунты в Google, GutHub, Spotify.
    - Смена пароля: Пользователь может изменить пароль или же сбросить по email, если забыл его.

## 2.2 Профиль пользователя:

- Основные функции:
    - Профиль: Авторизованный пользователь получает свой профиль.
    - Редактирования профиля: Пользователь может редактировать свой профиль: фотографию профиля, свое имя и раздел о себе

# 3.0 Стек:

- Python  3.12
- Django5
- Bootstrap5

![Снимок экрана 2024-06-22 в 19.11.53.png](..%2F..%2FDesktop%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-22%20%D0%B2%2019.11.53.png)

## Полезные ссылки или где я брал вдохновение:

- [Reset Password](https://www.youtube.com/watch?v=sFPcd6myZrY&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=21)
- [Login and register with django](https://github.com/earthcomfy/Django-registration-and-login-system)

## Tutorial

Если я не поленюсь, обязательно сделаю.

**Quick Start**

To get this project up and running locally on your computer follow the following steps.

1. Set up a python virtual environment
2. Run the following commands

```bash
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver

```

3. Open a browser and go to http://localhost:8000/