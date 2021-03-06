from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}  # Protegendo o email!
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criado',
            'modificado',
            'ativo',
        )

    def validate_avaliacao(self, valor):  # noqa
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('O valor precisa ser umm número inteiro entre 1 e 5.')


class CursoSerializer(serializers.ModelSerializer):

    media_avaliacoes = serializers.SerializerMethodField()

    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criado',
            'modificado',
            'ativo',
            'avaliacoes',
            'media_avaliacoes',
        )

    def get_media_avaliacoes(self, obj):  # noqa
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2
