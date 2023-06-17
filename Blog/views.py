from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<html><title>Алексей Стогов</title><h1>Сайт Алексея Стогова</h1></html>' )
