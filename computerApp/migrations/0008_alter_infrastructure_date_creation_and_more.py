# Generated by Django 4.0.3 on 2022-06-12 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0007_rename_nom_infrastructure_infrastructure_infrastructure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 13, 31, 2, 738154)),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 13, 31, 2, 738141)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 13, 31, 2, 713760)),
        ),
        migrations.AlterField(
            model_name='personnelle',
            name='date_entree',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 13, 31, 2, 737797)),
        ),
    ]