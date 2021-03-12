from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()  # noqa
    serializer_class = CursoSerializer
