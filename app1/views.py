from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff

# Create your views here.

#
# def index(request):
#     obj=Staff.objects.get(id=1)
#     return render(request,'adarsh.html',{'a':obj})

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def service(request):
    return render(request,'service.html')


