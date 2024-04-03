from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.log_out),
    path("python_intro/", views.python_introduction, name ="python_intro"),
    path("error/", views.error, name="error"),
    path("python_syntax/", views.python_syntax, name = "python_syntax"), 
    path("create/", views.create, name = "create")
]