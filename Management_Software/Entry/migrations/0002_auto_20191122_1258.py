# Generated by Django 2.2.7 on 2019-11-22 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]
