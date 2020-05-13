from django.contrib import admin

# Register your models here.
from AnalizzaVocabolario.models import Testo, Parola, TestoParola

admin.site.register(Testo)
admin.site.register(Parola)
admin.site.register(TestoParola)