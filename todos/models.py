from django.db import models
from datetime import date

class Todo(models.Model):
    titulo = models.CharField(verbose_name='Título',max_length=100,null=False,blank=False)
    criacao_dt = models.DateTimeField(auto_now_add=True,null=False,blank=False)
    entrega_dt = models.DateField(verbose_name='Data de Entrega',null=False,blank=False)
    finalizacao_dt = models.DateField(null=True)

    class Meta:
        ordering = ["entrega_dt"]

    def mark_has_complete(self):
        if not self.finalizacao_dt:
            self.finalizacao_dt = date.today()
            self.save()