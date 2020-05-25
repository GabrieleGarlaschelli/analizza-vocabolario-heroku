from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User
from AnalizzaVocabolario.models import Testo, Parola, TestoParola, ParolaInBlacklist
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from AnalizzaVocabolario.services.CalculateIC import calculateIC
from AnalizzaVocabolario.services.SplitText import tokenize


class CreateUserForm(UserCreationForm):
    """Forms per creare utente"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class PasswordChange(PasswordChangeForm):
    """Forms per cambiare password utente"""
    helper = FormHelper()
    helper.form_id = 'add_test_form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Modifica password'))


class AddtextCrispyForm(forms.Form):
    """Forms per creare un testo privato o publico"""
    titolo = forms.CharField(max_length=120, min_length=3)
    testo = forms.CharField(max_length=1000000, help_text='Incolla qui il tuo testo', widget=forms.Textarea)
    link = forms.URLField(max_length=250, required=False)
    privato = forms.BooleanField(required=False, help_text='Clicca per rendere il testo privato')

    helper = FormHelper()
    helper.form_id = 'add_test_form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Aggiungi'))


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


class ModifyUserForm(forms.ModelForm):
    """Forms per modificare dati utente """
    helper = FormHelper()
    helper.form_id = 'modify_user_form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Salva'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class AddWordToBlacklist(forms.Form):
    """Forms per mettere una parola in  blacklist
    :param parola:Aggiunge una parola in blackilist """
    parola = forms.CharField(max_length=20, help_text='Inserisci la parola da aggiungere alla blacklist', min_length=1)

    helper = FormHelper()
    helper.form_id = 'add_test_form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Inserisci'))

    def save(self, user):
        data = self.cleaned_data
        parolabl = ParolaInBlacklist(parolabl=data['parola'], user=user)
        ParolaInBlacklist.save(parolabl)

