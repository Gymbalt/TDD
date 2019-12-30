from django.shortcuts import render


# Создайте ваши представления здесь.
def home_page(request):
    """домашняя страница"""
    return render(request, 'home.html')