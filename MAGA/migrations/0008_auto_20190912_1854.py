# Generated by Django 2.2.4 on 2019-09-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAGA', '0007_auto_20190912_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaded_photo',
            name='photo_ad',
            field=models.ImageField(upload_to='./Media/upload'),
        ),
    ]