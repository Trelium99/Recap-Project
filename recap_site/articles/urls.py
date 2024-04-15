from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path("login", views.login, name="login-page"),
    path("register", views.register, name="register-page"),
    path("all_reads", views.all_reads, name="all_reads"),
    path('posts/<slug:posts_slug>', views.posts, name="single_posts"),
    path('logout', views.logout, name="logout")
]
