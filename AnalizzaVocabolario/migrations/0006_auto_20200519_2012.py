# Generated by Django 3.0.6 on 2020-05-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizzaVocabolario', '0005_auto_20200519_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testo',
            name='titolo',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]