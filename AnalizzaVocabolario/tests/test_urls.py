from django.contrib.auth.models import User
from django.test import TestCase, Client, client
from django.urls import reverse
from AnalizzaVocabolario.models import TestoParola,Parola,Testo
import json

# raccolta test per le views #

class TestViews(TestCase):
    def test_add_text_url(self):
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:add-text'))
        self.assertEquals(response.status_code, 302)

    def test_features_text_url(self):
        client = Client()
        response=client.get(reverse('AnalizzaVocabolario:features-text',args=[2]))
        self.assertEquals(response.status_code,302)

    def test_homepage_url(self):
        client = Client()
        response=client.get(reverse('AnalizzaVocabolario:homepage'))
        self.assertEquals(response.status_code,302)

    def test_delete_text_url(self):
        client = Client()
        response=client.get(reverse('AnalizzaVocabolario:delete-text', args=[2]))
        self.assertEquals(response.status_code,302)

    def test_personal_text_url(self):
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:personal-text'))
        self.assertEquals(response.status_code, 302)

    def test_user_create_url(self):
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:user-register'))
        self.assertEquals(response.status_code, 200)

    def test_search_titles_url(self):
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:search'))
        self.assertEquals(response.status_code, 302)

    def test_login_url(self):
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:login'))
        self.assertEquals(response.status_code, 200)

    def test_logout_url(self):
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:logout'))
        self.assertEquals(response.status_code, 302)






