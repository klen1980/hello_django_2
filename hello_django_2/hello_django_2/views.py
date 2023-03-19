from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 5+6
    return render(request, 'about.html', {'greting': a})

def reverse (request):
    usertext = request.GET['username']
    reverced= usertext[::-1]
    return render(request, 'reverse.html', {'word': reverced})

def home (request):
    return HttpResponse ('This is my homepage')
