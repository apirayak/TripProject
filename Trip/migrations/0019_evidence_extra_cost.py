# Generated by Django 2.1.7 on 2019-04-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0018_remove_evidence_extra_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='extra_cost',
            field=models.FloatField(default=0),
        ),
    ]