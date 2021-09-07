from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python!"}
    return render(request, "index.html", context=data)


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def products(request, product_id=21):
    output = "<h2>Product № {0}</h2>".format(product_id)
    return HttpResponse(output)


def users(request, id, name):
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)
