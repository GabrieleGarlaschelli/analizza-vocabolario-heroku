from django.contrib.auth.models import User
from django.test import TestCase
from AnalizzaVocabolario.models import TestoParola,Parola,Testo,ParolaInBlacklist

# raccolta test per i models #

class TestModels(TestCase):


    def setUp(self):
        """"Inizializzazione"""
        user = User.objects.create_user('john', 'john@email.com', 'johnpassword')
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
        self.blackList=ParolaInBlacklist.objects.create(
            parolabl='label',
        user = user
        )


    def test_testo(self):
        """"Test del modello Testo"""
        self.assertEqual(self.testo.titolo,'titolo1')
        self.assertEqual(self.testo.link,'www.ciao.it')
        self.assertEqual(self.testo.privato,False)
        self.assertEqual(self.testo.IC, 30.22)
        self.assertEqual(self.testo.author.username,'john')
        self.assertEqual(self.testo.author.email, 'john@email.com')

    def test_not_valid_testo(self):
        self.assertNotEqual(self.testo.titolo,'tito')
        self.assertNotEqual(self.testo.link,'wwiao.it')
        self.assertNotEqual(self.testo.privato,True)
        self.assertNotEqual(self.testo.IC, 29.21)
        self.assertNotEqual(self.testo.author.username,'john1')
        self.assertNotEqual(self.testo.author.email, 'john1@email.com')


    def test_parola(self):
        """"Test del modello Parola"""
        self.assertEqual(self.parola.termine,'ciaooo')

    def test_not_valid_parola(self):
        self.assertNotEqual(self.parola.termine,'ciao')


    def test_testoparola(self):
        """"Test del modello TestoParola"""
        self.assertEqual(self.testo_parola.frequenza, 99)

    def test_not_valid_testoparola(self):
        self.assertNotEqual(self.testo_parola.frequenza, 2)


    def test_parolaInBlackList(self):
        """"Test del modello Parola in blackList"""
        self.assertEqual(self.blackList.parolabl,'label')
        self.assertEqual(self.blackList.user.username,'john')
        self.assertEqual(self.blackList.user.email, 'john@email.com')

    def test_not_valid_parolaInBlackList(self):
        self.assertNotEqual(self.blackList.parolabl,'label1')
        self.assertNotEqual(self.blackList.check,False)
        self.assertNotEqual(self.blackList.user.username,'john1')



