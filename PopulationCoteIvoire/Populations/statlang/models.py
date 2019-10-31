from django.db import models
from django.db.models import Sum
# Create your models here.

class Poputlations(models.Model):
    nom=models.CharField(max_length=255)
    nombreHabitant=models.PositiveIntegerField()
    @property
    def poucentage(self):
        pc =self.nombreHabitant/100
        return pc 
    @property
    def max(self):
        poucent = Poputlations.objects.all().aggregate(total = Sum('nombreHabitant'))
        print(poucent)
        return poucent
    
    def __str__(self):
        return self.nom