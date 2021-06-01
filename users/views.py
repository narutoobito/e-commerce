from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import Cart
# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        a=User.objects.filter()
        print(a)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('shop:index'))
        else:
            return render(request, "users/index.html", {"message": "invalid username or password"})

    return render(request, "users/index.html")


def signup(request):
    if request.method=="POST":
        username = request.POST["uname"]
        password = request.POST["pword"]
        first= request.POST["firstname"]
        last= request.POST["lastname"]
        email= request.POST["email"]
        try:
            check= User.objects.get(username=username)
        except User.DoesNotExist:
            check = None
        if check==None:
            user = User.objects.create_user(username, email, password)
            user.first_name = first
            user.last_name = last
            user.save()
            return HttpResponseRedirect(reverse('users:index'), {"user":user})

    return render(request,"users/signup.html")

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("shop:index"))

def cart(request):
    try:
        user_cart = Cart.objects.filter(owner=request.user)
    except Cart.DoesNotExist:
        user_cart = None;
    return render(request,"shop/cart.html", {"owned": user_cart})

