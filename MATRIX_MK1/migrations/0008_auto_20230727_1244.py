# Generated by Django 3.2.20 on 2023-07-27 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MATRIX_MK1', '0007_alter_datatable_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatable',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 27, 12, 44, 57, 731451)),
        ),
    ]
