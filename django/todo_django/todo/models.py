from django.db import models

# Create your models here.
class Todo(models.Model):
     discription = models.CharField(max_length=128)
     is_done = models.BooleanField(default=False)
     fecha = models.DateField()
     unidades = models.IntegerField()

