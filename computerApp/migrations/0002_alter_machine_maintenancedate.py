# Generated by Django 4.0.3 on 2022-05-25 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 25, 12, 57, 27, 630608)),
        ),
    ]
