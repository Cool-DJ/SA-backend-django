# Generated by Django 2.1.13 on 2020-10-27 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_costing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dockroute',
            name='is_exclude_destination',
            field=models.BooleanField(db_column='IsExcludeDestination', default=True),
        ),
        migrations.AddField(
            model_name='dockroute',
            name='is_exclude_source',
            field=models.BooleanField(db_column='IsExcludeSource', default=True),
        ),
    ]
