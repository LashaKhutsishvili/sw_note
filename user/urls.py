from django.urls import path

from user import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", views.login.as_view(), name='login'),
    path("logout/", views.logout.as_view(), name='logout')
]