from django.db import models
from django.core.validators import MaxValueValidator


class Movie(models.Model):
    title = models.CharField('Título', max_length=255)
    description = models.TextField('Descrição', blank=True)
    rate = models.IntegerField(
        'Avaliação', default=0, validators=[MaxValueValidator(5)])

    class Meta():
        ordering = ['-rate']
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.title
