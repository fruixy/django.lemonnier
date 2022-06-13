# Generated by Django 4.0.3 on 2022-06-13 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0019_alter_infrastructure_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 0, 21, 20, 488977)),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 0, 21, 20, 488964)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 0, 21, 20, 464792)),
        ),
        migrations.AlterField(
            model_name='personnelle',
            name='date_entree',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 0, 21, 20, 488648)),
        ),
    ]
