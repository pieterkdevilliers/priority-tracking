# Generated by Django 4.1.5 on 2023-01-31 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0003_rename_actiondate_action_action_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='priority',
            field=models.ForeignKey(blank=True, limit_choices_to={'activeStatus': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='actions.priority'),
        ),
    ]