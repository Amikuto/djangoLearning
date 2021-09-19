from django.db import models


# Create your models here.


# class Employee(models.Model):
#     last_name = models.CharField("Фамилия", max_length=64)
#     first_name = models.CharField("Имя", max_length=64)
#     patronymic = models.CharField("Отчество", max_length=64)
#     address = models.CharField("Место жительства", max_length=200)
#     email = models.CharField("Email", max_length=128)
#     phone = models.CharField("Номер телефона", max_length=20)
#     age = models.IntegerField("Возраст")
#
#     def __str__(self):
#         return f"Фамилия: {self.last_name} Имя:{self.first_name}"
