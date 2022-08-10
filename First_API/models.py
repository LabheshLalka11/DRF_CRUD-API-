from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name