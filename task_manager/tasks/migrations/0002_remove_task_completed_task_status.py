# Generated by Django 4.2.4 on 2023-09-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], default='Incomplete', max_length=20),
        ),
    ]
