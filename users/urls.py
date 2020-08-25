from django.urls import path
from . import views

app_name = "users"

urlpatterns=[
        path("", views.index, name="index"),
        path("signup/", views.signup,name="signup"),
        path("signout/", views.signout, name="signout"),
        path("cart/", views.cart, name="cart"),
        ]
