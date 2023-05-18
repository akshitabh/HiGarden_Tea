from django.db import models
class Person(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()

class Product(models.Model):
    discription=models.TextField()
    upload_img=models.ImageField(upload_to='product/')
 
# Create your models here.
