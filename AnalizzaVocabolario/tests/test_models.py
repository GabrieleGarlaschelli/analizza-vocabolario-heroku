from django.contrib.auth.models import User
from django.test import TestCase
from AnalizzaVocabolario.models import TestoParola,Parola,Testo

# raccolta test per i models #

class TestModels(TestCase):
    def setUp(self):
        user = User.objects.create()
        self.testo=Testo.objects.create(
            titolo='titolo1',
            link='www.ciao.it',
            privato=False,
            author=user,
            IC=30.22
        )
        self.parola=Parola.objects.create(
            termine='ciaooo'
        )
        self.testo_parola = TestoParola.objects.create(
            testo=self.testo,
        parola = self.parola,
        frequenza = 99
        )

    def test_testo(self):
        self.assertEqual(self.testo.titolo,'titolo1')
        self.assertEqual(self.testo.link,'www.ciao.it')
        self.assertEqual(self.testo.privato,False)
        self.assertEqual(self.testo.IC, 30.22)

    def test_not_valid_testo(self):
        self.assertNotEqual(self.testo.titolo,'tito')
        self.assertNotEqual(self.testo.link,'wwiao.it')
        self.assertNotEqual(self.testo.privato,True)
        self.assertNotEqual(self.testo.IC, 29.21)




    def test_parola(self):
        self.assertEqual(self.parola.termine,'ciaooo')

    def test_not_valid_parola(self):
        self.assertNotEqual(self.parola.termine,'ciao')




    def test_testoparola(self):
        self.assertEqual(self.testo_parola.frequenza, 99)

    def test_not_valid_testoparola(self):
        self.assertNotEqual(self.testo_parola.frequenza, 2)

