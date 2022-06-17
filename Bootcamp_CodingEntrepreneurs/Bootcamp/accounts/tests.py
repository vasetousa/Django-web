from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings

# Create your tests here.

User = get_user_model()


class UserTestCase(TestCase):
    '''
    setting up creating the user
    '''

    def setUp(self):
        user_a = User(username='vasil', email='vasetousa@gmail.com')
        # user.objects.create()
        # user.objects.create_user()
        user_a_pw = '1234'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

    def test_user_exist(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password_is_correct(self):
        # user_qs = User.objects.filter(username__iexact='vasil')     # not needed, but if you want to check again
        # user_exists = user_qs.exists() and user_qs.count() == 1
        # self.assertTrue(user_exists)
        # self.assertEqual(self.user_pw, '1234')
        # user_a = user_qs.first()
        user_a = User.objects.get(username='vasil')
        self.assertTrue(user_a.check_password(self.user_a_pw))

    def test_login_url(self):
        # login_url = '/login/'
        # self.assertEqual(settings.LOGIN_URL, login_url)
        login_url = settings.LOGIN_URL
        # self.client.get, self.client.post - 2 requests we are focusing in
        data = {'username': 'vasil', 'password': self.user_a_pw}
        response = self.client.post(login_url, data, follow=True)
        print(dir(response))
        status_code = response.status_code
        redirect_path = response.request.get('PATH_INFO')
        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)

