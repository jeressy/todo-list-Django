from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(verbose_name="Título",max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega",null=False, blank=False)
    finished_at = models.DateTimeField(null=True)



