from django.test import TestCase,SimpleTestCase
from AnalizzaVocabolario.services.SplitText import tokenize


class Test(TestCase):
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore"


    def test_simple(self):
        self.assertTrue(True)


    def test_coma_remove(self):
        tokenizeText = tokenize(self.text)
        self.assertTrue(',' not in tokenizeText)


    def test_word_count(self):
        tokenizeText = tokenize(self.text)
        word_count=0
        for k,v in tokenizeText.items():
            word_count+=v
        self.assertTrue(word_count==15)

