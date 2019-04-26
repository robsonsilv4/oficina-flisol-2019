from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from movies.models import Movie


class MovieCreateView(CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:list')
    # template_name_suffix = '_form'


class MovieListView(ListView):
    model = Movie
    fields = '__all__'
    # template_name_suffix = '_list'


class MovieDetailView(DetailView):
    model = Movie
    fields = '__all__'
    # template_name_suffix = '_detail'


class MovieUpdateView(UpdateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:list')
    # template_name_suffix = '_form'


class MovieDeleteView(DeleteView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:list')
    # template_name_suffix = '_confirm_delete'
