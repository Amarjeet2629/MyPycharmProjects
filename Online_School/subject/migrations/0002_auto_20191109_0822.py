# Generated by Django 2.2.7 on 2019-11-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
