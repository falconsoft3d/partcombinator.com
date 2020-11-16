from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return render(request, "basecombinator/basecombinator.html")

def apps(request):
    return render(request, "basecombinator/apps.html")