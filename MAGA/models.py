from django.db import models


# Create database models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    ip_ad = models.CharField(max_length=15, null=False)
    pass


class Uploaded_photo(models.Model):
    id = models.AutoField(primary_key=True)
    photo_ad = models.ImageField(upload_to='img')
    photo_tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reversed('MAGA:pic_detail', args=[str(self.id)])



class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    discription = models.CharField(max_length=200)
    pass




