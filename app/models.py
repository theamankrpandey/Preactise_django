from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30,null=True)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    contact=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    Name = models.CharField(max_length=30)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.Name