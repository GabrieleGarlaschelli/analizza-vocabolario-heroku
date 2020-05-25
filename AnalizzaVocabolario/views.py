from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, View
from django.core import serializers
from AnalizzaVocabolario.forms import CreateUserForm, AddtextCrispyForm, ModifyUserForm, PasswordChange, \
    AddWordToBlacklist
from AnalizzaVocabolario.models import Testo, TestoParola, ParolaInBlacklist
from django.shortcuts import render, redirect
from django.db.models import Q


# Create your views here.

@login_required()
def search_titles(request):
    """QUESTO METODO CI SERVE PER TROVARE DEI TESTI TRAMITE IL TITOLO"""
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        filtro = request.GET.get("filtro", None)
        if Testo.objects.filter(titolo__contains=filtro).exists():
            testi_list = Testo.objects.filter(titolo__contains=filtro).filter(Q(privato=False) | Q(author=request.user))
            testi = serializers.serialize('json', testi_list, fields=('author_id', 'id', 'link', 'titolo'))
            return JsonResponse(testi, status=200, safe=False)
        else:
            return JsonResponse({'status': False}, status=200)
    return JsonResponse({}, status=400)



class UserCreateView(CreateView):
    """QUESTA CLASSE CI SERVE PER LA CREAZIONE DI UN NUOVO UTENTE"""
    form_class = CreateUserForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('AnalizzaVocabolario:login')


@login_required()
def PersonalTextList(request):
    """QUESTO METODO CI SERVE PER CARICARE I TESTI PERSONALI"""
    testi = Testo.objects.filter(author=request.user).order_by('id').reverse()
    return render(request, 'AnalizzaVocabolario/personalText.html', {'object_list': testi})


@login_required()
def Homepage(request):
    """QUESTO METODO CI SERVE PER CARICARE I TESTI NEL HOMEPAGE"""
    testi = Testo.objects.filter(Q(privato=False) | Q(author=request.user)).order_by('id').reverse()[:10]
    return render(request, 'AnalizzaVocabolario/homepage.html', {'object_list': testi})


class DeleteText(LoginRequiredMixin, DeleteView):
    """QUESTA CLASSE CI SERVE PER ELIMINARE UN TESTO"""
    def get(self, request):
        id1 = request.GET.get('id', None)
        Testo.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


@login_required()
def add_text(request):
    """QUESTO METODO CI SERVE PER AGGIUNGERE UN TESTO """
    if request.method == "POST":
        form = AddtextCrispyForm(request.POST)
        if form.is_valid():
            form.save(request.user)

        return redirect('AnalizzaVocabolario:homepage')
    else:
        form = AddtextCrispyForm()
        return render(request, 'AnalizzaVocabolario/addText.html', {'form': form})


@login_required()
def featuresText(request, pk):
    """QUESTO METODO CI SERVE PER ACCEDERE AI FEATURES DI UN  TESTO """
    testoparola = TestoParola.objects.filter(testo_id=pk)
    return render(request, 'AnalizzaVocabolario/featuresText.html', {'object_list': testoparola})

@login_required()
def allwords(request):
    """QUESTO METODO CI SERVE PER ANALIZZARE TUTTI I TESTI"""
    return_dict = dict()
    testoparola = TestoParola.objects.all()
    for p in testoparola:
        if (return_dict.get(p.parola.termine, None)==None):
            return_dict.update({p.parola.termine:p.frequenza})
        else:
            return_dict[p.parola.termine]+=p.frequenza
    return render(request, 'AnalizzaVocabolario/analyzeAllWords.html', {'object_list': return_dict})


@login_required()
def allPersonalWords(request):
    """QUESTO METODO CI SERVE PER ANALIZZARE TUTTI I TESTI PERSONALI"""
    return_dict = dict()
    testoparola = TestoParola.objects.filter(Q(testo__author=request.user))
    for p in testoparola:
        if (return_dict.get(p.parola.termine, None)==None):
            return_dict.update({p.parola.termine:p.frequenza})
        else:
            return_dict[p.parola.termine]+=p.frequenza
    return render(request, 'AnalizzaVocabolario/analyzeAllPersonalWords.html', {'object_list': return_dict})



class ShowProfile(LoginRequiredMixin, DetailView):
    """QUESTA CLASSE CI SERVE PER LA VISUALIZZAZIONE DEL PROPRIO PROFILO"""
    model = User
    template_name = 'AnalizzaVocabolario/profile.html'


class ModifyUser(LoginRequiredMixin, UpdateView):
    """QUESTA CLASSE CI SERVE PER LA MODIFICA DEL PROFILO"""
    model = User
    template_name = 'AnalizzaVocabolario/modificauser.html'
    form_class = ModifyUserForm
    success_url = reverse_lazy('AnalizzaVocabolario:profile')

    def get_success_url(self):
        """QUESTO METODO CI SERVE PER MODIFICARE IL PROFILO UTENTE"""
        user_id = self.kwargs['pk']
        return reverse_lazy('AnalizzaVocabolario:profile', kwargs={'pk': user_id})

@login_required()
def PasswordChangeView(request):
    """QUESTO METODO CI SERVE PER CAMBIARE IL PASSWORD DI UTENTE"""
    if request.method == 'POST':
        form = PasswordChange(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('AnalizzaVocabolario:profile', pk=request.user.id)
    else:
        form = PasswordChange(request.user)
    return render(request, 'AnalizzaVocabolario/password_change.html', {'form': form})

@login_required()
def blacklist(request):
    """QUESTO METODO CI SERVE PER CARICARE LE PAROLE DELLA BLACKLIST IN UNA TABELLA"""
    if request.method == "POST":
        form = AddWordToBlacklist(request.POST)
        if form.is_valid():
            form.save(request.user)
        return redirect('AnalizzaVocabolario:blacklist')
    else:
        form = AddWordToBlacklist()

    parole = ParolaInBlacklist.objects.filter(user=request.user).order_by('id').reverse()
    return render(request, 'AnalizzaVocabolario/blacklist.html', {'form': form, 'object_list': parole})


class DeleteBlacklist(LoginRequiredMixin,View):
    """QUESTO METODO CI SERVE PER ELIMINARE LE PAROLE DALLA BLACKLIST"""
    def get(self, request):
        parolaid = request.GET.get('parola', None)
        print(parolaid)
        ParolaInBlacklist.objects.get(id=parolaid).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@login_required()
def returnBlacklist(request):
    """QUESTO METODO CI SERVE PER ACCEDERE ALLA BLACKLIST"""
    listWords = ParolaInBlacklist.objects.filter(user=request.user)
    list_words = serializers.serialize('json', listWords, fields=('parolabl'))
    return JsonResponse(list_words, status=200, safe=False)


@login_required()
def graphSingleText(request, pk):
    """QUESTO METODO CI SERVE PER VEDERE L'ANALISI GRAFICA DI UN TESTO"""
    titolo = Testo.objects.get(id=pk)
    print(titolo)
    testoparola = TestoParola.objects.filter(testo_id=pk)
    return render(request, 'AnalizzaVocabolario/graph.html', {'object_list': testoparola, 'titolo':titolo})


@login_required()
def graphPersonalText(request):
    """QUESTO METODO CI SERVE PER VEDERE L'ANALISI GRAFICA DI TESTI PERSONALI"""
    return_dict = dict()
    testoparola = TestoParola.objects.filter(Q(testo__author=request.user))
    for p in testoparola:
        if (return_dict.get(p.parola.termine, None)==None):
            return_dict.update({p.parola.termine:p.frequenza})
        else:
            return_dict[p.parola.termine]+=p.frequenza
    return render(request, 'AnalizzaVocabolario/graphPersonalText.html', {'object_list': return_dict})


@login_required()
def graphAllText(request):
    """QUESTO METODO CI SERVE PER VEDERE L'ANALISI GRAFICA DI TUTTI I TESTI"""
    return_dict = dict()
    testoparola = TestoParola.objects.all()
    for p in testoparola:
        if (return_dict.get(p.parola.termine, None)==None):
            return_dict.update({p.parola.termine:p.frequenza})
        else:
            return_dict[p.parola.termine]+=p.frequenza
    return render(request, 'AnalizzaVocabolario/graphAllText.html', {'object_list': return_dict})

@login_required()
def check_text_is_unique(request):
    """QUESTO METODO CI SERVE PER GARANTIRE CHE IL TITOLO SIA UNICO"""
    title = None
    titolo = request.GET.get('titolo', False)
    if titolo:
        title = Testo.objects.filter(titolo=titolo)
    return JsonResponse({'is_not_unique': True if title else False})

@login_required()
def select_for_compare(request):
    """QUESTO METODO CI SERVE PER SELEZIONARE DUE TESTI DA CONFRONTARE"""
    testi = Testo.objects.filter(Q(privato=False) | Q(author=request.user))
    return render(request, 'AnalizzaVocabolario/selectForCompare.html', {'object_list': testi})

@login_required()
def compare_text(request, key_testi1, key_testi2):
    """QUESTO METODO CI SERVE PER CONFRONTARE DUE TESTI"""
    testo1 = TestoParola.objects.filter(testo_id=key_testi1)
    testo2 = TestoParola.objects.filter(testo_id=key_testi2)
    return render(request, 'AnalizzaVocabolario/compare.html', {'testo1': testo1, 'testo2': testo2})