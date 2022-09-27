# Generated by Django 2.1.13 on 2022-05-04 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0056_auto_20220503_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessorialdetentionoverride',
            name='request_source_id',
            field=models.ForeignKey(db_column='RequestSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialdetentionoverridehistory',
            name='request_source_id',
            field=models.ForeignKey(db_column='RequestSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialoverride',
            name='request_source_id',
            field=models.ForeignKey(db_column='RequestSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialoverridehistory',
            name='request_source_id',
            field=models.ForeignKey(db_column='RequestSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverride',
            name='request_source_id',
            field=models.ForeignKey(db_column='RequestSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverridehistory',
            name='request_source_id',
            field=models.ForeignKey(db_column='RequestSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AlterField(
            model_name='accessorialoverridehistory',
            name='acc_header_version_id',
            field=models.ForeignKey(db_column='AccHeaderVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialHeaderHistory'),
        ),
        migrations.AlterField(
            model_name='accessorialstorageoverridehistory',
            name='request_version_id',
            field=models.ForeignKey(db_column='RequestVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.RequestHistory'),
        ),
    ]
