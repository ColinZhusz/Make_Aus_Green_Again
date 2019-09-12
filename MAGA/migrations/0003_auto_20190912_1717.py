# Generated by Django 2.2.4 on 2019-09-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAGA', '0002_auto_20190906_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='uploaded_photo',
            name='photo_tag',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Uploaded_photo',
        ),
    ]
