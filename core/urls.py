from django.contrib.auth import views
from django.urls import path
from .views import home, contacts
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("account/", views.account, name="account"),
    path("logout/", views.logout_view, name="logout"),
]
