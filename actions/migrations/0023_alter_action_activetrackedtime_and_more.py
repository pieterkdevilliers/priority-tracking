# Generated by Django 4.1.4 on 2023-01-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0022_alter_action_activetrackedtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='activeTrackedTime',
            field=models.DurationField(blank=True, default='00:00:00.0', null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='trackedTime',
            field=models.DurationField(blank=True, default='00:00:00.0', null=True),
        ),
    ]
