from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Poputlations)

class PoputlationsAdmin(admin.ModelAdmin):
    
    list_display=('nom','nombreHabitant','poucentage','max')
    