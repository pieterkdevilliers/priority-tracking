# Generated by Django 4.1.5 on 2023-01-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0006_rename_date_action_actiondate'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='trackedStart',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='trackedStop',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]