from django.shortcuts import render
from django.http import request
from .models import FormData

# Create your views here.
def index(request):
    if request.method=='POST':
      name=request.POST['name']
      phone=request.POST['phone']
      email=request.POST['email']
      address=request.POST['address']
      data = FormData(name=name, phone=phone, email=email, address=address)
      data.save()
      print(name, phone, email, address)
    return render(request, 'index.html')
