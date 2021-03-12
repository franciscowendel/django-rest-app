from django.db import models


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField('Título', max_length=150)
    url = models.URLField('URL', default=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(decimal_places=1, max_digits=2)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']
        ordering = ['id']
