# Generated by Django 4.1.5 on 2023-01-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0009_action_activetimetracked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='activeTimeTracked',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='trackedStart',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='trackedStop',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='trackedTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]