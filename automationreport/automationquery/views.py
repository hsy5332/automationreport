from django.shortcuts import render
from automationquery import models
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
