# Generated by Django 4.0.3 on 2022-06-12 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0013_alter_infrastructure_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 17, 1, 54, 373783)),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 17, 1, 54, 373770)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 17, 1, 54, 350278)),
        ),
        migrations.AlterField(
            model_name='personnelle',
            name='date_entree',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 17, 1, 54, 373443)),
        ),
    ]
