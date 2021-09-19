from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Customer


# Create your views here.
def services(request):
    employee = Employee.objects.all()
    return render(request, 'services/appointment.html', {"employees": employee})
