from django.db import models


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    pass
