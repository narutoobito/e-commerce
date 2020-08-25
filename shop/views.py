from django.shortcuts import render, HttpResponseRedirect
from shop.models import Products
from django.urls import reverse
from users.models import Cart
# Create your views here.


def index(request):
    #if not request.user.is_authenticated:
     #   return HttpResponseRedirect(reverse("users:index"))
    product = Products.objects.all()
    print(product.first().product_image.url)
    return render(request, "shop/index.html",
                  {
                      "product": product,
                  })


def buy(request, value):
    product = Products.objects.get(id=value)
    return render(request, "shop/buyScreen.html", {"product": product})


def addtocart(request, id):
    product = Products.objects.get(id=id)
    cart_element = Cart.objects.filter(product=product).filter(owner=request.user)

    if not cart_element.first():
        cart = Cart(owner=request.user, product=product)
        cart.save()
        owned = Cart.objects.filter(owner=request.user)
        return render(request, "shop/cart.html", {"owned": owned})

    else:
        return HttpResponseRedirect(reverse("users:cart"))


def removefromCart(request, id):
    object = Cart.objects.get(id=id)
    object.delete()
    owned = Cart.objects.filter(owner=request.user)
    return render(request, "shop/cart.html", {"owned": owned})

