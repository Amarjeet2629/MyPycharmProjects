# Generated by Django 2.2.7 on 2019-11-22 14:35

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0006_auto_20191122_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='checkin_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='checkout_time',
            field=models.TimeField(blank=True),
        ),
    ]
