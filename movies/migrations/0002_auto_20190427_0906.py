# Generated by Django 2.2 on 2019-04-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watched',
        ),
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.IntegerField(default=0, verbose_name='Avaliação'),
        ),
    ]
