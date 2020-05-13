from django.contrib.auth.models import User
from django.test import TestCase,Client,SimpleTestCase
from AnalizzaVocabolario.forms import CreateUserForm,AddtextCrispyForm

# raccolta test per i forms #

class Setup_class(TestCase):
    def setUp(self):
        self.user=User.objects.create(firstnam="baljinder",
                                      last_name="singh",
                                      username="balli356",
                                      email="229896@gmail.it",
                                      password1="ciao1234",
                                      password2="ciao1234"
                                      )


class TestFormsRegistration(TestCase):
    def test_create_user_form_valid_data(self):
        form=CreateUserForm(data={
            'firstname' :'baljinder',
            'last_name':'singh',
            'username':'balli356',
            'email':'229896@studenti.unimore.it',
            'password1':'ciao1234$',
            'password2':'ciao1234$'
        })
        self.assertTrue(form.is_valid())


    def test_create_user_form_password_not_valid(self):
        form = CreateUserForm(data={
            'firstname': 'bally',
            'last_name': 's',
            'username': 'bali356',
            'email': '229896@gmail.com',
            'password1': 'ciao123',
            'password2': 'ciao14$'
        })
        self.assertFalse(form.is_valid())

    def test_create_user_form_email_not_valid(self):
        form = CreateUserForm(data={
            'firstname': 'bally',
            'last_name': 's',
            'username': 'bali356',
            'email': 'fsdfsdf.it',
            'password1': 'ciao123',
            'password2': 'ciao123'
        })
        self.assertFalse(form.is_valid())


class TestFormsText(SimpleTestCase):

    def test_AddtextCrispyForm(self):
        form= AddtextCrispyForm(data={
            'titolo':'titolo1',
            'testo':'testo1',
            'link':'https://www.youtube.com/watch?v=zUl-Tf-UEzw&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=5',
            'privato':True,


        })
        self.assertTrue(form.is_valid())

    def test_not_valid_AddtextCrispyForm(self):
        form = AddtextCrispyForm(data={
            'titolo': '',
            'testo': 'testo1',
            'link': 'https://www.youtube.com/watch?v=zUl-Tf-UEzw&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=5',
            'privato': True,

        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)


