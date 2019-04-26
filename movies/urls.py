from django.urls import path
from movies.views import *

urlpatterns = [
    path('adicionar/', MovieCreateView.as_view(), name='movie-create'),
    path('listar/', MovieListView.as_view(), name='movie-list'),
    path('detalhes/', MovieDetailView.as_view(), name='movie-detail'),
    path('atualizar/', MovieUpdateView.as_view(), name='movie-update'),
    path('deletar/', MovieDeleteView.as_view(), name='movie-delete'),
]
