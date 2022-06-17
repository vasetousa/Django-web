from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


# Create your tests here.
class OrderTestCase(TestCase):
    def setUp(self):
        user_a = User(username='vasil', email='vasetousa@gmail.com')
        # user.objects.create()
        # user.objects.create_user()
        user_a_pw = '1234'
        self.user_a = user_a
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()


    #  TDD - test driven development - write the test and then the code
    # def test_create_order(self):
    #     obj = Order.objects.create(user=self.user_a, product=product_a)
