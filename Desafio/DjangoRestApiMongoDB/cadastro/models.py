from email.policy import default
from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=200,blank=False, default='')
    telefone = models.CharField(max_length=70, blank=False, default='')
    endereco = models.CharField(max_length=200,blank=False, default='')
    profissao = models.CharField(max_length=50,blank=False, default='')
    curriculo = models.ImageField(default='')