from django.db import models

# Create your models here.

class Poputlations(models.Model):
    nom=models.CharField(max_length=255)
    nombreHabitant=models.PositiveIntegerField()
    def __str__(self):
        return self.nom