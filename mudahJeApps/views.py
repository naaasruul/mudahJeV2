from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.
def page(request):
    
    return render(request, 'home.html')

def pilihPerbualan(request):
    return render(request, 'pilihPerbualan.html')