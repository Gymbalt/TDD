from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Создайте ваши представления здесь.
def home_page(request: HttpRequest):
    """домашняя страниц"""
    return HttpResponse('<html><title>To-Do lists</title></html>')