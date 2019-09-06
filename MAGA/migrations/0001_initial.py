# Generated by Django 2.2.4 on 2019-09-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_ad', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Uploaded_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_ad', models.CharField(max_length=200)),
                ('photo_tag', models.ManyToManyField(to='MAGA.Tag')),
            ],
        ),
    ]
