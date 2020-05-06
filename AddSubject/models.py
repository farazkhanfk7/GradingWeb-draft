from django.db import models

# Create your models here.
class Subject(models.Model):
    Subject_Name = models.CharField(max_length=200)
    Subject_Code = models.CharField(max_length=200)
    Max_Marks = models.IntegerField()
    Course = models.CharField(max_length=200)
    Branch = models.CharField(max_length=200)
    Semester = models.IntegerField()

class Mark(models.Model):
    marks_obtain = models.IntegerField()
    upload = models.FileField(upload_to='marksheet')

class Student(models.Model):
    studname = models.CharField(max_length=100)
    studroll = models.IntegerField(primary_key=True, editable=True)
    coursename = models.CharField(max_length=100)
    branchname = models.CharField(max_length=100)
    sem = models.IntegerField()