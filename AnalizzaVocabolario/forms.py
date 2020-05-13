from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User

from AnalizzaVocabolario.models import Testo, Parola, TestoParola
from django.contrib.auth.forms import UserCreationForm

from AnalizzaVocabolario.services.CalculateIC import calculateIC
from AnalizzaVocabolario.services.SplitText import tokenize


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


def calcolaIC(param):
    pass


class AddtextCrispyForm(forms.Form):
    titolo = forms.CharField(max_length=120, min_length=3)
    testo = forms.CharField(max_length=1000000, help_text='Incolla qui il tuo testo', widget=forms.Textarea)
    link = forms.URLField(max_length=250, required=False)
    privato = forms.BooleanField(required=False, help_text='Clicca per rendere testo privato')

    helper = FormHelper()
    helper.form_id = 'add_test_form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

    def save(self, user):
        data = self.cleaned_data
        complessità= calculateIC(data['testo'])
        testo = Testo(titolo=data['titolo'], link=data['link'], privato=data['privato'], author=user, IC=complessità)
        Testo.save(testo)
        ris = tokenize(data['testo'])
        for k, v in ris.items():
            if Parola.objects.filter(termine=k).exists():
                tp = TestoParola(parola=Parola.objects.get(termine=k), testo=Testo.objects.get(titolo=data['titolo']),
                                 frequenza=v)
                tp.save(force_insert=True)
            else:
                par = Parola(termine=k)
                par.save(force_insert=True)
                tp = TestoParola(parola=Parola.objects.get(termine=k), testo=Testo.objects.get(titolo=data['titolo']),
                                 frequenza=v)
                tp.save(force_insert=True)
