# Generated by Django 2.1.13 on 2022-07-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0025_auto_20220727_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terminalhistory',
            name='city_version',
        ),
        migrations.AddField(
            model_name='terminal',
            name='postal_code',
            field=models.TextField(db_column='PostalCode', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='terminalhistory',
            name='postal_code',
            field=models.TextField(db_column='PostalCode', max_length=10, null=True),
        ),
    ]
