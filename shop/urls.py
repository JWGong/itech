from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Home.as_view()),
    path("home/", views.Home.as_view(),name="home"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.handleLogout, name="logout"),
    path("dish/", views.DishView.as_view(), name="dish"),
    path("search/", views.search, name="search"),
    path("register/", views.Register.as_view(), name="register")
]
