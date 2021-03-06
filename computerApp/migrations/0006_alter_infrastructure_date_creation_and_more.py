# Generated by Django 4.0.3 on 2022-06-12 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0005_alter_infrastructure_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 8, 42, 520801)),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 8, 42, 520788)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 8, 42, 497735)),
        ),
        migrations.AlterField(
            model_name='personnelle',
            name='date_entree',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 8, 42, 520442)),
        ),
    ]
