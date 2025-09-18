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

    path("add_restaurant/", views.add_restaurant,name="add_restaurant"),

    path("add_restaurant/open_update_restaurant/<int:restaurant_id>", views.open_update_restaurant,name="open_update_restaurant"),

    path("signin1/open_show_restaurant/",views.open_show_restaurant, name="open_show_restaurant"),

    path('update_restaurant/<int:restaurant_id>',views.update_restaurant,name="update_restaurant"),

    path("delete_restaurant/<int:restaurant_id>",views.delete_restaurant,name="delete_restaurant")

]