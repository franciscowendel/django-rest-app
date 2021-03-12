from django.urls import path
from .views import (
    CursosAPIView,
    CursoAPIView,
    AvaliacoesAPIView,
    AvaliacaoAPIView,

)
urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
]
