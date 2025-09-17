from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.login),
    path("signin/",views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),

    path("signup1/",views.signup1,name="signup1"),
    path("signin1/",views.signin1,name="signin1"),

    path("signin1/add_restaurant_page/", views.add_restaurant_page, name="add_restaurant_page"),

    path("add_restaurant/", views.add_restaurant,name="add_restaurant")

]