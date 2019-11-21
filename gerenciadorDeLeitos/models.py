from django.db import models

class Leito(models.Model):
    STATUS_DE_LIMPEZA = [
        ('AL', 'Aguardando limpeza'),
        ('EL', 'Em limpeza'),
        ('LI', 'Limpo'),
    ]

    codigo = models.IntegerField()
    predio = models.TextField()
    ala = models.TextField()
    andar = models.IntegerField()
    status_limpeza = models.CharField(max_length=2, choices=STATUS_DE_LIMPEZA, default='LI')

    def __str__(self):
        return self.predio
