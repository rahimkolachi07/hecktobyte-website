from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mode1(request):
    return render(request,'index.html')
def mode2(request):
    return render(request,'about.html')
def mode3(request):
    return render(request,'service.html')
def mode4(request):
    return render(request,'team.html')
def mode5(request):
    return render(request,'why.html')
def mode5(request):
    return render(request,'tools.html')