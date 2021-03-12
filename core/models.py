from django.db import models


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)

