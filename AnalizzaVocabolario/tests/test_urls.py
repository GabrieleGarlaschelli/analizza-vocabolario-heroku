from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.test import TestCase, Client, client
from django.urls import reverse
from AnalizzaVocabolario.models import TestoParola,Parola,Testo,ParolaInBlacklist
import json

# raccolta test per le views #
class TestUrl(TestCase):
    def test_add_text_url(self):
        """"Test delle urls di add text"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:add-text'))
        self.assertEquals(response.status_code, 302)

    def test_features_text_url(self):
        """"Test delle urls di features"""
        client = Client()
        response=client.get(reverse('AnalizzaVocabolario:features-text',args=[2]))
        self.assertEquals(response.status_code,302)

    def test_homepage_url(self):
        """"Test delle urls di home Page"""
        client = Client()
        response=client.get(reverse('AnalizzaVocabolario:homepage'))
        self.assertEquals(response.status_code,302)

    def test_delete_text_url(self):
        """"Test delle urls di delete text"""
        client = Client()
        response=client.get(reverse('AnalizzaVocabolario:delete-text'))
        self.assertEquals(response.status_code,302)

    def test_personal_text_url(self):
        """"Test delle urls  di testi personali"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:personal-text'))
        self.assertEquals(response.status_code, 302)

    def test_user_create_url(self):
        """"Test delle urls crea utente"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:user-register'))
        self.assertEquals(response.status_code, 200)

    def test_search_titles_url(self):
        """"Test delle urls di cerca testi"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:search'))
        self.assertEquals(response.status_code, 302)


    def test_logout_url(self):
        """"Test delle urls di logout"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:logout'))
        self.assertEquals(response.status_code, 302)

    def test_ModifyUser(self):
        """"Test delle urls di modifica utente"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:modificauser', args=[2]))
        self.assertEquals(response.status_code, 302)

    def test_allwords(self):
        """"Test delle urls di visulizza tutte le parole"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:analyze-all-words'))
        self.assertEquals(response.status_code, 302)

    def test_profile(self):
        """"Test delle urls di profilo utente"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:profile', args=[2]))
        self.assertEquals(response.status_code, 302)


    def test_blackList(self):
        """"Test delle urls di parole da mettere in black List"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:blacklist'))
        self.assertEquals(response.status_code, 302)

    def test_graphSingleText(self):
        """"Test delle urls grafo di singolo testo"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:graph',args=[3]))
        self.assertEquals(response.status_code, 302)

    def test_graphAllText(self):
        """"Test delle urls grafo di tutti i testi"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:graph-all-text'))
        self.assertEquals(response.status_code, 302)


    def test_graphPersonalText(self):
        """"Test delle urls grafo di testo personale """
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:graph-personal-text'))
        self.assertEquals(response.status_code, 302)



    def test_Delete_blackList(self):
        """"Test delle urls di elimina una parola da blacklist"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:delete-blacklist',None))
        self.assertEquals(response.status_code, 302)


    def test_blackList_return(self):
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:return-blacklist',None))
        self.assertEquals(response.status_code, 302)


    def test_select_Text(self):
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:select-text'))
        self.assertEquals(response.status_code, 302)


    def test_compare_Text(self):

        """"Test delle urls di comparare due  testi"""
        client = Client()
        response = client.get(reverse('AnalizzaVocabolario:compare-text',args=[3,2]))
        self.assertEquals(response.status_code, 302)






    """  def test_login_url(self):
        client = Clientt()
        response = client.get(reverse('AnalizzaVocabolario:login'))
        self.assertEquals(response.status_code, 200)
    """







