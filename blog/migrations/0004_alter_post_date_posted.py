# Generated by Django 5.0.1 on 2024-01-17 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_date_posted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 17, 4, 8, 1, 512117, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
