# Generated by Django 2.1.13 on 2022-04-26 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0013_auto_20220412_1423'),
        ('pre_costing', '0020_auto_20220421_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spotquotemargin',
            name='sub_service_level_id',
        ),
        migrations.RemoveField(
            model_name='spotquotemarginhistory',
            name='sub_service_level_version_id',
        ),
        migrations.AddField(
            model_name='spotquotemargin',
            name='service_level_id',
            field=models.ForeignKey(db_column='ServiceLevelID', null=True, on_delete=django.db.models.deletion.CASCADE, to='pac.ServiceLevel'),
        ),
        migrations.AddField(
            model_name='spotquotemarginhistory',
            name='service_level_version_id',
            field=models.ForeignKey(db_column='ServiceLevelVersionID', null=True, on_delete=django.db.models.deletion.CASCADE, to='pac.ServiceLevelHistory'),
        ),
    ]
