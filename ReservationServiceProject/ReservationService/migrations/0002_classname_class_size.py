# Generated by Django 3.0.5 on 2020-05-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationService', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classname',
            name='class_size',
            field=models.IntegerField(default=30),
        ),
    ]
