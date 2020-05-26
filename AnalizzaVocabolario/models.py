from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class Testo(models.Model):
    """Creazione del modello Testo per registrare i testi inseriti"""
    titolo = models.CharField(max_length=120, unique=True)
    link = models.URLField(max_length=250, null=True, blank=True)
    privato = models.BooleanField()
    IC = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    data_creazione = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Testi'

    def __str__(self):
        return self.titolo


class Parola(models.Model):
    """Creazione del modello Parola per salvare tutti i termini presenti nei testi"""
    termine = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Parole'

    def save(self,*args,**kwargs):
        self.termine = self.termine.lower()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.termine


class TestoParola(models.Model):
    """Creazione del modello TestoParola che associa una parola ad un testo"""
    testo = models.ForeignKey(Testo, on_delete=models.CASCADE, related_name='testo')
    parola = models.ForeignKey(Parola, on_delete=models.CASCADE, related_name='parola')
    frequenza = models.IntegerField()


    class Meta:
        verbose_name_plural = 'TestoParole'

class ParolaInBlacklist(models.Model):
    """Creazione del modello ParolaInBlacklist per salvare le parole nell blacklist"""
    parolabl = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ParoleInBlacklist'

    def save(self,*args,**kwargs):
        self.parolabl = self.parolabl.lower()
        super().save(*args,**kwargs)
