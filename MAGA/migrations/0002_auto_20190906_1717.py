# Generated by Django 2.2.4 on 2019-09-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAGA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='uploaded_photo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
