from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import viewsets
from rest_framework import mixins


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()  # noqa
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()  # noqa
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()  # noqa
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            pass
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()  # noqa
    serializer_class = AvaliacaoSerializer


# USANDO viewsets

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()  # noqa
    serializer_class = CursoSerializer


class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Avaliacao.objects.all()  # noqa
    serializer_class = AvaliacaoSerializer
