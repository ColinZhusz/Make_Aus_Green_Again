from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    ip_ad = models.CharField(max_length=15,null= False)
    pass


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    discription = models.CharField(max_length=200)
    pass


class Uploaded_photo(models.Model):
    id = models.AutoField(primary_key=True)
    photo_ad = models.CharField(max_length=200,null= False)
    photo_tag = models.ManyToManyField(Tag)
    pass

