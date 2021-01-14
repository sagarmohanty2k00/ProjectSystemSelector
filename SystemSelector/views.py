from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def assign(request):
    return render(request, 'assign.html')


def show(request):
    return render(request, 'show.html')


def save(request):
    return render(request, 'show.html')


def clear(request):
    return render(request, 'index.html')
