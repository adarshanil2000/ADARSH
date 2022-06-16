from django.db import models

# Create your models here.
class Products(models.Model):
    item=models.CharField(max_length=100)
    stor=models.CharField(max_length=100)
    no_item=models.IntegerField()

class Staff(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()

class Course(models.Model):
    course_name=models.CharField(max_length=50)
    duration=models.IntegerField(50)
    units=models.IntegerField(50)

class Items(models.Model):
    name=models.CharField(max_length=50)
    item_number=models.IntegerField(50)

class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=50)

