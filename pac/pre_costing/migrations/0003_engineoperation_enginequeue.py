# Generated by Django 2.1.13 on 2022-09-23 14:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pre_costing', '0002_auto_20220922_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineOperation',
            fields=[
                ('OperationID', models.BigAutoField(db_column='OperationID', primary_key=True, serialize=False)),
                ('OperationName', models.CharField(db_column='OperationName', max_length=50)),
            ],
            options={
                'db_table': 'EngineOperation',
            },
        ),
        migrations.CreateModel(
            name='EngineQueue',
            fields=[
                ('EngineQueueID', models.BigAutoField(db_column='EngineQueueID', primary_key=True, serialize=False)),
                ('OperationBody', models.CharField(db_column='OperationBody', max_length=4000)),
                ('Description', models.CharField(db_column='Description', default='Operation pending ...', max_length=200)),
                ('DueDate', models.DateTimeField(db_column='DueDate', default=datetime.datetime.now)),
                ('CompletedOn', models.DateTimeField(blank=True, db_column='CompletedOn')),
                ('Completed', models.BooleanField(db_column='Completed', default=False)),
                ('Success', models.BooleanField(db_column='Success', default=False)),
                ('InProgress', models.BooleanField(db_column='InProgress', default=False)),
                ('Recurring', models.BooleanField(db_column='Recurring', default=False)),
                ('RecurringPattern', models.CharField(blank=True, db_column='RecurringPattern', default='{"pattern":"daily"}', max_length=200)),
                ('OperationID', models.ForeignKey(db_column='OperationID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pre_costing.EngineOperation')),
                ('RequestedBy', models.ForeignKey(db_column='RequestedBy', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'EngineQueue',
            },
        ),
    ]
