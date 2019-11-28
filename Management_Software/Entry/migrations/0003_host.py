# Generated by Django 2.2.7 on 2019-11-22 12:59

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Entry', '0002_auto_20191122_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('time_stamp', models.TimeField(blank=True)),
            ],
        ),
    ]
