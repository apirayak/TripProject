# Generated by Django 2.1.7 on 2019-04-01 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0017_auto_20190326_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidence',
            name='extra_cost',
        ),
    ]
