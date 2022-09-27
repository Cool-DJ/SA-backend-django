# Generated by Django 2.1.13 on 2022-08-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0119_freetime_tm_detention_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freetimehistory',
            name='base_version',
        ),
        migrations.RemoveField(
            model_name='freetimehistory',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='freetimehistory',
            name='is_latest_version',
        ),
        migrations.RemoveField(
            model_name='freetimehistory',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='freetimehistory',
            name='updated_on',
        ),
        migrations.AlterField(
            model_name='freetime',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='freetime',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='freetimehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='freetimehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
    ]
