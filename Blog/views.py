from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<html><title>Сайт Алексея Стогова</title><h1>Алексей Стогов</h1></html>' )
