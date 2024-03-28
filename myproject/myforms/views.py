from django.shortcuts import render
from django.http import request
from .models import FormData

# Create your views here.
def index(request):
    if request.method=='POST':
      name=request.POST['name']
      phone=request.POST['phone']
      data = FormData(name=name, phone=phone)
      data.save()
      print(name, phone)
    return render(request, 'index.html')
