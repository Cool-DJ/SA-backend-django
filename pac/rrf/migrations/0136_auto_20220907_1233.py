# Generated by Django 2.1.13 on 2022-09-07 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0135_auto_20220907_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessorialdetailhistory',
            name='commodity_version_id',
            field=models.ForeignKey(db_column='CommodityVersionID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.CommodityHistory'),
        ),
    ]
