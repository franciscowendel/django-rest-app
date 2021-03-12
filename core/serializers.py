from rest_framework import serializers
from .models import Curso, Avaliacao  # noqa


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}  # Protegendo o email!
        }
        model = Avaliacao
