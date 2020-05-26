from django.test import SimpleTestCase, Client
from django.urls import reverse_lazy

from AnalizzaVocabolario.views import search_titles, UserCreateView, Homepage, PersonalTextList, DeleteText, add_text, \
    featuresText, ModifyUser,ShowProfile,allwords,blacklist,DeleteBlacklist,graphAllText,graphPersonalText,graphSingleText,select_for_compare,compare_text,returnBlacklist

from django.urls import resolve, reverse

# raccolta test per le urls #

"""Test delle views"""
class TestViews(SimpleTestCase):

    def test_UserCreateView(self):
        """Test delle views di crea utente """
        url = reverse_lazy('AnalizzaVocabolario:user-register')
        self.assertEqual(resolve(url).func.view_class, UserCreateView)
    def test_not_valid_UserCreateView(self):
        url = reverse_lazy('AnalizzaVocabolario:personal-text')
        self.assertNotEqual(resolve(url).func, UserCreateView)


    def test_PersonalTextList_view(self):
            """Test delle views di testo personale """
            url = reverse('AnalizzaVocabolario:personal-text')
            self.assertEqual(resolve(url).func, PersonalTextList)
    def test_not_valid_PersonalTextList_view(self):
        url = reverse('AnalizzaVocabolario:delete-text',)
        self.assertNotEqual(resolve(url).func.view_class, PersonalTextList)


    def test_HomePage_view(self):
            """Test delle views di homepage """
            url = reverse('AnalizzaVocabolario:homepage')
            self.assertEqual(resolve(url).func, Homepage)
    def test_not_valid_HomePage_view(self):
            url = reverse('AnalizzaVocabolario:homepage')
            self.assertNotEqual(resolve(url).func, DeleteText)


    def test_DeleteText_view(self):
            """Test delle views di eliminare un testo"""
            url = reverse('AnalizzaVocabolario:delete-text')
            self.assertEqual(resolve(url).func.view_class, DeleteText)
    def test_Not_valid_DeleteText_view(self):
            url = reverse('AnalizzaVocabolario:delete-text')
            self.assertNotEqual(resolve(url).func.view_class, Homepage)


    def test_search_titles_view(self):
            """Test delle views di cerca testi """
            url = reverse('AnalizzaVocabolario:search')
            self.assertEqual(resolve(url).func, search_titles)
    def test_not_valid_search_titles_view(self):
            url = reverse('AnalizzaVocabolario:search')
            self.assertNotEqual(resolve(url).func, PersonalTextList)


    def test_personalText_view(self):
            """Test delle views di testi personali"""
            url = reverse('AnalizzaVocabolario:personal-text')
            self.assertEqual(resolve(url).func, PersonalTextList)
    def test_not_valid_personalText_view(self):
            url = reverse('AnalizzaVocabolario:personal-text')
            self.assertNotEqual(resolve(url).func, search_titles)


    def test_addText_view(self):
            """Test delle views di aggiungi testi"""
            url = reverse('AnalizzaVocabolario:add-text')
            self.assertEqual(resolve(url).func, add_text)
    def test_not_valid_addText_view(self):
            url = reverse('AnalizzaVocabolario:add-text')
            self.assertNotEqual(resolve(url).func, search_titles)


    def test_feature_view(self):
            """Test delle views di features """
            url=reverse('AnalizzaVocabolario:features-text',args=[99])
            self.assertEqual(resolve(url).func,featuresText)
    def test_features_not_valid_view(self):
            url=reverse('AnalizzaVocabolario:features-text',args=[99])
            self.assertNotEqual(resolve(url).func,search_titles)

    def test_modifyUser(self):
        """Test delle views di modifica dati di utente"""
        url=reverse('AnalizzaVocabolario:modificauser',args=[2])
        self.assertEqual(resolve(url).func.view_class, ModifyUser)
    def test_modifyUser(self):
        url=reverse('AnalizzaVocabolario:modificauser',args=[2])
        self.assertNotEqual(resolve(url).func.view_class, ShowProfile)

    def test_profile(self):
        """Test delle views di profilo"""
        url=reverse('AnalizzaVocabolario:profile',args=[2])
        self.assertEqual(resolve(url).func.view_class, ShowProfile)
    def test_profile(self):
        url = reverse('AnalizzaVocabolario:profile', args=[2])
        self.assertNotEqual(resolve(url).func.view_class, ModifyUser)

    def test_allwords(self):
        """Test delle views tutte le parole"""
        url=reverse('AnalizzaVocabolario:analyze-all-words')
        self.assertEqual(resolve(url).func, allwords)
    def test_allwords(self):
        url=reverse('AnalizzaVocabolario:analyze-all-words')
        self.assertNotEqual(resolve(url).func, ModifyUser)

    def test_blackList(self):
        """Test delle views di aggiungewre una parola in blacklist"""
        url = reverse('AnalizzaVocabolario:blacklist')
        self.assertEqual(resolve(url).func, blacklist)
    def test_blackList_notValid(self):
        url = reverse('AnalizzaVocabolario:blacklist')
        self.assertNotEqual(resolve(url).func, ModifyUser)

    def test_delete_blackList(self):
        """Test delle views eliminare una parola da blacklist"""
        url=reverse('AnalizzaVocabolario:delete-blacklist')
        self.assertEqual(resolve(url).func.view_class,DeleteBlacklist)
    def test_delete_blackList_not_valid(self):
        url = reverse('AnalizzaVocabolario:delete-blacklist')
        self.assertNotEqual(resolve(url).func.view_class, blacklist)



    def test_graphAllText(self):
        """Test delle views di graffo di tutti i testi"""
        url=reverse('AnalizzaVocabolario:graph-all-text')
        self.assertEqual(resolve(url).func,graphAllText)
    def test_not_valid_graphAllText(self):
        url = reverse('AnalizzaVocabolario:graph-all-text')
        self.assertNotEqual(resolve(url).func, blacklist)


    def test_graphPersonalText(self):
        """Test delle views di grafo di testi personali"""
        url=reverse('AnalizzaVocabolario:graph-personal-text')
        self.assertEqual(resolve(url).func,graphPersonalText)
    def test_not_valid_graphPersonalText(self):
        url = reverse('AnalizzaVocabolario:graph-personal-text')
        self.assertNotEqual(resolve(url).func, blacklist)

    def test_graphSingleText(self):
        """Test delle views di testi singoli"""
        url = reverse('AnalizzaVocabolario:graph',args=[3])
        self.assertEqual(resolve(url).func, graphSingleText)

    def test_not_valid_graphSingleText(self):
        url = reverse('AnalizzaVocabolario:graph',args=[3])
        self.assertNotEqual(resolve(url).func, blacklist)


    def test_blackList_return(self):
        """Test delle views di blackList return"""
        url = reverse('AnalizzaVocabolario:return-blacklist',None)
        self.assertEqual(resolve(url).func, returnBlacklist)

    def test_not_valid_blackList_return(self):
        url = reverse('AnalizzaVocabolario:return-blacklist',None)
        self.assertNotEqual(resolve(url).func, blacklist)



    def test_select_text(self):
        url = reverse('AnalizzaVocabolario:select-text')
        self.assertEqual(resolve(url).func, select_for_compare)

    def test_not_valid_select_text(self):
        url = reverse('AnalizzaVocabolario:select-text')
        self.assertNotEqual(resolve(url).func, blacklist)

    def test_compare_text(self):
        """Test delle views di comparare due testi"""
        url = reverse('AnalizzaVocabolario:compare-text', args=[2,3])
        self.assertEqual(resolve(url).func, compare_text)

    def test_not_valid_compare_text(self):
        url = reverse('AnalizzaVocabolario:compare-text',args=[3,4])
        self.assertNotEqual(resolve(url).func, blacklist)















