from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name='Título',max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name='Data de Entrega', null=False, blank=False)
    finished_at = models.DateField(null=True)

# ordenar por data de entrega mais recente
    class Meta:
        ordering = ['deadline']

# ordenar por data de entrega menos recente
#     class Meta:
#         ordering = ['-deadline']

def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()