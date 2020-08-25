from django.urls import path
from . import views

app_name="shop"

urlpatterns=[
    path("",views.index, name="index"),
    path("buy/<int:value>", views.buy, name="buy"),
    path("addtocart/<int:id>", views.addtocart, name="addtocart"),
    path("removefromCart/<int:id>", views.removefromCart, name="removefromCart")
]