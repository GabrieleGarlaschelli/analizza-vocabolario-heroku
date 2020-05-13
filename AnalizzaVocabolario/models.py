from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Testo(models.Model):
    titolo = models.CharField(max_length=120)
    link = models.URLField(max_length=250, null=True, blank=True)
    privato = models.BooleanField()
    IC = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Testi'

    def __str__(self):
        return self.titolo


class Parola(models.Model):
    termine = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Parole'


class TestoParola(models.Model):
    testo = models.ForeignKey(Testo, on_delete=models.CASCADE, related_name='testo')
    parola = models.ForeignKey(Parola, on_delete=models.CASCADE, related_name='parola')
    frequenza = models.IntegerField()

    class Meta:
        verbose_name_plural = 'TestoParole'

