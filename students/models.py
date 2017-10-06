from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=75)
    last_name=models.CharField(max_length=150)
    class_type = models.TextFiled(max_length=200)

# Create your models here.
