# Generated by Django 2.1.7 on 2019-03-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0002_auto_20190319_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start',
            field=models.CharField(default='', max_length=200),
        ),
    ]