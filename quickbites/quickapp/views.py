from django.shortcuts import render
from .models import*
import re
# Create your views here.
def open(request):
# return render(request,'admin.html')
    return render(request,'indexchatgpt.html')