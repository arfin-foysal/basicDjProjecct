# from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render


def home(request):
    text={
        "name":"arfin foysal",
        "age":23,
        "lang":["javaScript","java","python,"]
    }
    return render(request,'employee/home.html',text)

def about(request):
    return render(request,'employee/about.html')