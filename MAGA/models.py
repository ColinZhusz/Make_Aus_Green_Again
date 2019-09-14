from django.db import models


# Create database models here.
from django.views.generic import ListView, CreateView


class User(models.Model):
    id = models.AutoField(primary_key=True)
    ip_ad = models.CharField(max_length=15, null=False)
    pass


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    pass


class Uploaded_photo(models.Model):
    id = models.AutoField(primary_key=True)
    photo_ad = models.ImageField(upload_to='img')
    photo_tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reversed('MAGA:photo_ad', args=[str(self.id)])

