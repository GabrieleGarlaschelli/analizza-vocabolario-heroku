# Generated by Django 3.0.6 on 2020-05-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizzaVocabolario', '0002_auto_20200508_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testo',
            name='IC',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='testo',
            name='privato',
            field=models.BooleanField(),
        ),
    ]
