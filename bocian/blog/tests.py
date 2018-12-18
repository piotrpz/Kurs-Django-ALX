from django.test import TestCase

# Create your tests here.
from blog.models import Wpis


class TestBlogRoutes(TestCase):

    def test_main_page_of_blog_exists(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code,200)

class TestWpisModel(TestCase):
    def test_can_create_wpis(self):
        w = Wpis(tytul = "ala ma kota",
                 tresc = "Kot ma Ale")
        w.save()

        self.assertEqual(w,Wpis.objects.last())
        w.delete()