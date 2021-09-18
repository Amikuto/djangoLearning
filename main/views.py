from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def prices(request):
    return render(request, 'main/prices.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def feedback(request):
    return render(request, 'main/feedback.html')
