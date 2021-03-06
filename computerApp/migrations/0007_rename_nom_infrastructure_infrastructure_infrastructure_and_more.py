# Generated by Django 4.0.3 on 2022-06-12 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0006_alter_infrastructure_date_creation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infrastructure',
            old_name='nom_infrastructure',
            new_name='infrastructure',
        ),
        migrations.RenameField(
            model_name='infrastructure',
            old_name='nom_responsable',
            new_name='responsable',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='nom_machine',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='nom_utilisateur',
            new_name='responsable',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='responsable_maj',
            new_name='utilisateur',
        ),
        migrations.RenameField(
            model_name='personnelle',
            old_name='nom_infrastructure',
            new_name='infrastructure',
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 44, 12, 741372)),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 44, 12, 741360)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 44, 12, 718369)),
        ),
        migrations.AlterField(
            model_name='personnelle',
            name='date_entree',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 44, 12, 741036)),
        ),
    ]
