# Generated by Django 2.2.6 on 2019-10-13 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191013_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 14, 25, 24, 213237, tzinfo=utc)),
        ),
    ]
