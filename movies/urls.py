from django.urls import path
from movies.views import MovieCreateView, MovieListView, MovieDetailView, MovieUpdateView, MovieDeleteView

app_name = 'movies'
urlpatterns = [
    path('adicionar/', MovieCreateView.as_view(), name='create'),
    path('listar/', MovieListView.as_view(), name='list'),
    path('<int:pk>/detalhes/', MovieDetailView.as_view(), name='detail'),
    path('<int:pk>/atualizar/', MovieUpdateView.as_view(), name='update'),
    path('<int:pk>/deletar/', MovieDeleteView.as_view(), name='delete'),
]
