# Generated by Django 2.2.6 on 2019-10-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191013_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default='django.utils.timezone.now'),
        ),
    ]
