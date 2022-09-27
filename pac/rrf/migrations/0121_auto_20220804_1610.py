# Generated by Django 2.1.13 on 2022-08-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0120_auto_20220804_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lanetype',
            old_name='lane_type_nName',
            new_name='lane_type_name',
        ),
        migrations.AddField(
            model_name='freetimehistory',
            name='base_version',
            field=models.IntegerField(db_column='BaseVersion', default=None, null=True),
        ),
        migrations.AddField(
            model_name='freetimehistory',
            name='comments',
            field=models.TextField(db_column='Comments', default=None, null=True),
        ),
        migrations.AddField(
            model_name='freetimehistory',
            name='is_latest_version',
            field=models.BooleanField(db_column='IsLatestVersion', default=False, null=True),
        ),
        migrations.AddField(
            model_name='freetimehistory',
            name='updated_by',
            field=models.TextField(db_column='UpdatedBy', default=None, null=True),
        ),
        migrations.AddField(
            model_name='freetimehistory',
            name='updated_on',
            field=models.DateTimeField(db_column='UpdatedOn', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='accchargebehavior',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accchargebehavior',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accchargebehaviorhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accchargebehaviorhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetail',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetail',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetailhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetailhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetention',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetention',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetentionhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetentionhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetentionoverride',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetentionoverride',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetentionoverridehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialdetentionoverridehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialheader',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialheader',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialheaderhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialheaderhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialoverride',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialoverride',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialoverridehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialoverridehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialstorage',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialstorage',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialstoragehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialstoragehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialstorageoverride',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialstorageoverride',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialstorageoverridehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accessorialstorageoverridehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accfactor',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accfactor',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accfactorhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accfactorhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accrangetype',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accrangetype',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='accrangetypehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='accrangetypehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='commodityhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='commodityhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='customerzones',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='customerzones',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='customerzoneshistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='customerzoneshistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='freetimehistory',
            name='version_num',
            field=models.IntegerField(db_column='VersionNum', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='interlinercosts',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='interlinercosts',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='interlinercostshistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='interlinercostshistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='lanetype',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='lanetype',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='lanetypehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='lanetypehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='pointtype',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='pointtype',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='pointtypehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='pointtypehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='profitlosssummary',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='profitlosssummary',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='profitlosssummaryhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='profitlosssummaryhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='revenuebreakdown',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='revenuebreakdown',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='revenuebreakdownhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='revenuebreakdownhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='revenuehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='revenuehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='revenuehistoryhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='revenuehistoryhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='reviewhistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='reviewhistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='salesincentive',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='salesincentive',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='salesincentivehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='salesincentivehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='subpostalcode',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='subpostalcode',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='subpostalcodehistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='subpostalcodehistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='terms',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='terms',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
        migrations.AlterField(
            model_name='termshistory',
            name='is_active',
            field=models.BooleanField(db_column='IsActive', default=True),
        ),
        migrations.AlterField(
            model_name='termshistory',
            name='is_inactive_viewable',
            field=models.BooleanField(db_column='IsInactiveViewable', default=True),
        ),
    ]