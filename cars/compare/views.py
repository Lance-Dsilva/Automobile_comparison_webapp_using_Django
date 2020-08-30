from django.shortcuts import render
from .models import bike

def home(request):
    context = {}
    a = bike.objects.get(Name = 'Tvs apache RR310')
    context = {'a' : a}
    return render(request,'compare/index.html',context)