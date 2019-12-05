from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('resultados/',views.resultado,name='resultado'),
    path('pokemon/<int:pokemon_id>/',views.pokemon,name='pokemon')
]