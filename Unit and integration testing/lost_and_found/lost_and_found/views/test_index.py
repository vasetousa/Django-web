from django.test import TestCase, Client


class IndexRenderTest(TestCase):

    def setUp(self):
        self.test_client = Client()

    def test_getPostsIndex_shouldRenderTemplate(self):
        response = self.test_client.get('')
        self.assertTemplateUsed(response, 'index.html')
