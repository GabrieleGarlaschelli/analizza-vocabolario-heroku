from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.core import serializers
from AnalizzaVocabolario.forms import CreateUserForm, AddtextCrispyForm
from AnalizzaVocabolario.models import Testo, TestoParola
from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import random
# Create your views here.

@login_required()
def search_titles(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        filtro = request.GET.get("filtro", None)
        if Testo.objects.filter(titolo__contains=filtro).exists():
            testi_list = Testo.objects.filter(titolo__contains=filtro)
            testi = serializers.serialize('json', testi_list, fields=('author_id','id','link','titolo'))
            return JsonResponse(testi, status=200, safe=False)
        else:
            return JsonResponse({'status': False}, status=200)
    return JsonResponse({}, status=400)

"""
@login_required()
def UserCreateView(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            to_list = [form.email, settings.EMAIL_HOST_USER]
            subject='thank you for registration'
            message='Please confirm your id by inserting the pin./n '+str(random.randit(0,9999)
            from_email=settings.EMAIL_HOST_USER
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            messages.success(request,'Thank you')

            # PARTE DI INVIO EMAIL
        return redirect('AnalizzaVocabolario:logib')
    else:
        form = CreateUserForm()
        return render(request, 'AnalizzaVocabolario/registration/create_user.html', {'form': form})
"""
class UserCreateView(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('AnalizzaVocabolario:login')


@login_required()
def PersonalTextList(request):
    testi = Testo.objects.filter(author=request.user).order_by('id').reverse()
    return render(request, 'AnalizzaVocabolario/personalText.html', {'object_list': testi})

@login_required()
def Homepage(request):
    testi = Testo.objects.filter(privato=False).order_by('id').reverse()[:10]
    return render(request, 'AnalizzaVocabolario/homepage.html', {'object_list': testi})


class DeleteText(LoginRequiredMixin, DeleteView):
    model = Testo
    template_name = 'AnalizzaVocabolario/deleteText.html'
    success_url = reverse_lazy('AnalizzaVocabolario:homepage')

@login_required()
def add_text(request):
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
    testoparola = TestoParola.objects.filter(testo_id=pk)
    return render(request, 'AnalizzaVocabolario/featuresText.html', {'object_list':testoparola})



