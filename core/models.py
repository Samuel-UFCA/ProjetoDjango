from django.db import models


class Curso(models.Model):
    codigo_inep = models.IntegerField(unique=True)
    nome = models.CharField(max_length=255)
    grau = models.CharField(max_length=255)