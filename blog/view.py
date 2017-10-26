from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def contact(request):
    return render(request, 'contact.html')
