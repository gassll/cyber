from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages


def home(request):
    return render(request, 'core/home.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return redirect("account")

        return render(request, "registration/login.html", {
            "error": "Неверный логин или пароль"
        })

    return render(request, "registration/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # проверки
        if password1 != password2:
            return render(request, "registration/register.html", {
                "error": "Пароли не совпадают"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "registration/register.html", {
                "error": "Пользователь уже существует"
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request, user)
        return redirect("account")

    return render(request, "registration/register.html")


@login_required
def account(request):
    return render(request, "registration/account.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # просто можно сохранить/обработать данные (пока ничего не делаем с почтой)
        print(name, email, phone, message)

        messages.success(request, "Сообщение успешно отправлено!")

        return redirect("contacts")

    return render(request, "contacts.html")