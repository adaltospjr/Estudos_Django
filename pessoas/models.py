from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
