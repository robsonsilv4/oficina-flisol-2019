from django.db import models


class Movie(models.Model):
    title = models.CharField('Título', max_length=255)
    description = models.TextField('Descrição', blank=True)
    watched = models.BooleanField('Assistido?', default=False)

    class Meta():
        ordering = ['title']
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.title
