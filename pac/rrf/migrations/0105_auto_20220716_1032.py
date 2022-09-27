# Generated by Django 2.1.13 on 2022-07-16 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0104_auto_20220711_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_status_type',
            field=models.ForeignKey(db_column='RequestStatusTypeID', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.RequestStatusType'),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='request_status_type_version',
            field=models.ForeignKey(blank=True, db_column='RequestStatusTypeVersionID', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.RequestStatusTypeHistory'),
        ),
    ]
