# Generated by Django 5.0.1 on 2024-01-17 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 17, 4, 6, 58, 616494, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
