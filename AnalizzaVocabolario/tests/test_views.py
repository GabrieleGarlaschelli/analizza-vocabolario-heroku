from django.test import SimpleTestCase, Client
from django.urls import reverse_lazy

from AnalizzaVocabolario.views import search_titles, UserCreateView, Homepage, PersonalTextList, DeleteText, add_text,featuresText

from django.urls import resolve, reverse

# raccolta test per le urls #

class TestUrls(SimpleTestCase):

    def test_UserCreateView(self):
        url = reverse_lazy('AnalizzaVocabolario:user-register')
        self.assertEqual(resolve(url).func.view_class, UserCreateView)
    def test_not_valid_UserCreateView(self):
        url = reverse_lazy('AnalizzaVocabolario:personal-text')
        self.assertNotEqual(resolve(url).func, UserCreateView)


    def test_PersonalTextList_view(self):
            url = reverse('AnalizzaVocabolario:personal-text')
            self.assertEqual(resolve(url).func, PersonalTextList)
    def test_not_valid_PersonalTextList_view(self):
        url = reverse('AnalizzaVocabolario:delete-text',args=[99])
        self.assertNotEqual(resolve(url).func.view_class, PersonalTextList)


    def test_HomePage_view(self):
            url = reverse('AnalizzaVocabolario:homepage')
            self.assertEqual(resolve(url).func, Homepage)
    def test_not_valid_HomePage_view(self):
            url = reverse('AnalizzaVocabolario:homepage')
            self.assertNotEqual(resolve(url).func, DeleteText)


    def test_DeleteText_view(self):
            url = reverse('AnalizzaVocabolario:delete-text',args=[99])
            self.assertEqual(resolve(url).func.view_class, DeleteText)
    def test_Not_valid_DeleteText_view(self):
            url = reverse('AnalizzaVocabolario:delete-text',args=[44])
            self.assertNotEqual(resolve(url).func.view_class, Homepage)


    def test_search_titles_view(self):
            url = reverse('AnalizzaVocabolario:search')
            self.assertEqual(resolve(url).func, search_titles)
    def test_not_valid_search_titles_view(self):
            url = reverse('AnalizzaVocabolario:search')
            self.assertNotEqual(resolve(url).func, PersonalTextList)


    def test_personalText_view(self):
            url = reverse('AnalizzaVocabolario:personal-text')
            self.assertEqual(resolve(url).func, PersonalTextList)
    def test_not_valid_personalText_view(self):
            url = reverse('AnalizzaVocabolario:personal-text')
            self.assertNotEqual(resolve(url).func, search_titles)


    def test_addText_view(self):
            url = reverse('AnalizzaVocabolario:add-text')
            self.assertEqual(resolve(url).func, add_text)
    def test_not_valid_addText_view(self):
            url = reverse('AnalizzaVocabolario:add-text')
            self.assertNotEqual(resolve(url).func, search_titles)


    def test_feature_view(self):
            url=reverse('AnalizzaVocabolario:features-text',args=[99])
            self.assertEqual(resolve(url).func,featuresText)
    def test_features_not_valid_view(self):
            url=reverse('AnalizzaVocabolario:features-text',args=[99])
            self.assertNotEqual(resolve(url).func,search_titles)





