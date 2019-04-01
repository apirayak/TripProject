# Generated by Django 2.1.7 on 2019-04-01 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0020_employee_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='project',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='employee_name',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='project_name',
        ),
        migrations.AddField(
            model_name='trip',
            name='employee',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Trip.Employee'),
        ),
        migrations.AddField(
            model_name='trip',
            name='project',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Trip.Project'),
        ),
    ]
