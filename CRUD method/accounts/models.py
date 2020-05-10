from django.db import models

# Create your models here.
class Testmodel(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files')

class formmodel(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)