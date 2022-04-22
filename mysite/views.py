from django.http  import HttpResponse
from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html')
def page_3(request):
    return render(request, 'page.html')
def page_1(request):
    return render(request, 'page_1.html')
