from django.shortcuts import render
from .models import *
from django.db.models import Avg,Max,Min
# Create your views here.
def home(request):
    
    allInfo=Poputlations.objects.all().order_by('-nombreHabitant')
    data={
        'allinfo':allInfo
    }
    return render(request,'index.html',data)

def stat(request):
    allInfo=Poputlations.objects.all().order_by('-nombreHabitant')
    data={
        'allinfo':allInfo
    }
    return render(request,'statistique.html',data)