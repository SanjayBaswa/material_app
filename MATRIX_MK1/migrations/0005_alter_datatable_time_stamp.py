# Generated by Django 4.2.3 on 2023-07-21 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MATRIX_MK1", "0004_alter_datatable_time_stamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datatable",
            name="time_stamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 21, 17, 15, 3, 598970)
            ),
        ),
    ]
