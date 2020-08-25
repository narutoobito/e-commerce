from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Products
from users.models import Cart

# Create your tests here.


class ProductCases(TestCase):
    def setUp(self):
        u = User.objects.create_user("aaa", "bbb", "ccc")
        u.save()
        p1 = Products.objects.create(name="Aaa", product_type="Bbb", price="1rs", description="Ccc", product_image="aaa")
        p2 = Products.objects.create(name="Zzz", product_type="Zzz", price="1rs", description="Zzz", product_image="aaa")
        Cart.objects.create(owner=u, product=p1)

    def checkCart(self):
        d = Cart.objects.all()
        self.assertEqual(d.count(), 1)

    def flightCount(self):
        p = Products.objects.all()
        self.assertEqual(p.count(), 2)

    def test_index(self):
        e = Client()
        response = e.get("/shop/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"].count(), 2)

    def test_buy(self):
        p = Products.objects.first()
        c = Client()
        response = c.get(f"/shop/buy/{p.id}")
        self.assertEqual(response.status_code, 200)

    def test_addtocart(self):
        p = Products.objects.get(name="Zzz")
        u = User.objects.create(username='testuser')
        u.set_password('12345')
        u.save()
        c = Client()
        c.login(username='testuser', password='12345')
        cart = Cart.objects.all()
        response = c.get(f"/shop/addtocart/{p.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["owned"].count(), 1)
        self.assertEqual(cart.count(), 2)

    def test_delete(self):
        cart= Cart.objects.first()
        u = User.objects.create(username='testuser')
        u.set_password('12345')
        u.save()
        c = Client()
        c.login(username='testuser', password='12345')
        response= c.get(f"/shop/removefromCart/{cart.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["owned"].count(), 0)
