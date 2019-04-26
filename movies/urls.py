from django.urls import path
from movies.views import *

urlpatterns = [
    path('/adicionar', MovieCreateView.as_view(), 'movie-create'),
    path('/listar', MovieListView.as_view(), 'movie-list'),
    path('/detalhes', MovieDetailView.as_view(), 'movie-detail'),
    path('/atualizar', MovieUpdateView.as_view(), 'movie-update'),
    path('/deletar', MovieDeleteView.as_view(), 'movie-delete'),
]
