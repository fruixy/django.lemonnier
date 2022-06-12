# Generated by Django 4.0.3 on 2022-06-12 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0003_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom_infrastructure', models.CharField(max_length=1)),
                ('nom_responsable', models.CharField(max_length=15)),
                ('nb_machine', models.CharField(max_length=12)),
                ('maintenanceDate', models.DateField(default=datetime.datetime(2022, 6, 12, 9, 2, 25, 879607))),
                ('date_creation', models.DateField(default=datetime.datetime(2022, 6, 12, 9, 2, 25, 879619))),
            ],
        ),
        migrations.RenameField(
            model_name='personnelle',
            old_name='infrastructure',
            new_name='nom_infrastructure',
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 2, 25, 857246)),
        ),
        migrations.AlterField(
            model_name='personnelle',
            name='date_entree',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 2, 25, 879277)),
        ),
        migrations.AlterField(
            model_name='personnelle',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
