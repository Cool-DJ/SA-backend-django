# Generated by Django 2.1.13 on 2022-09-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0149_auto_20220922_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customerhistory',
            name='city_version',
        ),
        migrations.AddField(
            model_name='requestsectionlane',
            name='cost',
            field=models.TextField(db_column='Cost', default='[]'),
        ),
    ]
