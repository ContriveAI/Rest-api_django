from django.db import models
import datetime

# Create your models here.:


class Article(models.Model):
    name =  models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.IntegerField(blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True) 
    


    def __str__(self):
        return self.title
