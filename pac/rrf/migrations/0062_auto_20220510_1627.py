# Generated by Django 2.1.13 on 2022-05-10 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0061_auto_20220510_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessorialdetentionoverride',
            name='request_source_id',
        ),
        migrations.RemoveField(
            model_name='accessorialdetentionoverridehistory',
            name='request_source_id',
        ),
        migrations.RemoveField(
            model_name='accessorialoverride',
            name='request_source_id',
        ),
        migrations.RemoveField(
            model_name='accessorialoverridehistory',
            name='request_source_id',
        ),
        migrations.RemoveField(
            model_name='accessorialstorageoverride',
            name='request_source_id',
        ),
        migrations.RemoveField(
            model_name='accessorialstorageoverridehistory',
            name='request_source_id',
        ),
        migrations.RemoveField(
            model_name='requesthistory',
            name='request_source_id',
        ),
        migrations.RemoveField(
            model_name='requestsectionlanehistory',
            name='request_section_lane_source_id',
        ),
        migrations.RemoveField(
            model_name='requestsectionlanepricingpointhistory',
            name='request_section_lane_pricing_point_source_id',
        ),
        migrations.AddField(
            model_name='accessorialdetentionoverride',
            name='acc_detention_override_source_id',
            field=models.BigIntegerField(db_column='AccDetentionOverrideSourceID', null=True),
        ),
        migrations.AddField(
            model_name='accessorialdetentionoverridehistory',
            name='acc_detention_override_source_id_version_id',
            field=models.ForeignKey(db_column='AccDetentionOverrideSourceIDVersionID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialDetentionOverride'),
        ),
        migrations.AddField(
            model_name='accessorialoverride',
            name='acc_override_source_id',
            field=models.BigIntegerField(db_column='AccOverrideSourceID', null=True),
        ),
        migrations.AddField(
            model_name='accessorialoverridehistory',
            name='acc_override_source_id_version_id',
            field=models.ForeignKey(db_column='AccOverrideSourceIDVersionID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialOverride'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverride',
            name='acc_storage_override_source_id',
            field=models.BigIntegerField(db_column='AccStorageOverrideSourceID', null=True),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverridehistory',
            name='acc_storage_override_source_id_version_id',
            field=models.ForeignKey(db_column='AccStorageOverrideSourceIDVersionID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialStorageOverride'),
        ),
        migrations.AddField(
            model_name='requestsectionlanehistory',
            name='request_section_lane_source_id_version_id',
            field=models.ForeignKey(db_column='RequestSectionLaneSourceIDVersionID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.RequestSectionLane'),
        ),
        migrations.AddField(
            model_name='requestsectionlanepricingpointhistory',
            name='request_section_lane_pricing_point_source_id_version_id',
            field=models.ForeignKey(db_column='RequestSectionLanePricingPointSourceIDVersionID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.RequestSectionLanePricingPoint'),
        ),
        migrations.AddField(
            model_name='terms',
            name='status',
            field=models.BooleanField(db_column='Status', default=False),
        ),
        migrations.AddField(
            model_name='termshistory',
            name='status_version_id',
            field=models.ForeignKey(db_column='StatusVersionID', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Terms'),
        ),
    ]
