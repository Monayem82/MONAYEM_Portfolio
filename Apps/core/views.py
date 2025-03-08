from django.shortcuts import render

def home(request):
    return render(request,'core/index.html')

def home2(request):
    return render(request,'core/index2.html')