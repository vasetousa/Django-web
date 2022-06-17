from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
User = get_user_model()

'''
test if 'staff' user get access and non 'staff' user does not.
'''


class ProductTestCase(TestCase):

    def setUp(self):
        user_a = User(username='vasil', email='vasetousa@gmail.com')
        user_b = User.objects.create_user('doncho', 'doncho@abv.bg', '4321')
        user_a_pw = '1234'
        user_b_pw = '4321'
        self.user_a_pw = user_a_pw
        self.user_b_pw = user_b_pw
        self.user_a = user_a
        self.user_b = user_b
        user_a.is_staff = True
        user_a.is_superuser = False
        user_b.is_superuser = False
        user_a.set_password(user_a_pw)
        user_b.set_password(user_b_pw)
        user_a.save()
        user_b.save()

    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_invalid_request(self):
        self.client.login(username=self.user_b, password=self.user_b_pw)
        response = self.client.post('/', {'title': 'this is a valid test'})

        self.assertTrue(response.status_code != 200)
        print(response.status_code)

    def test_valid_request(self):
        self.client.login(username=self.user_a, password=self.user_a_pw)
        response = self.client.post('/', {'title': 'this is a valid test'})

        self.assertTrue(response.status_code == 200)
        print(response.status_code)