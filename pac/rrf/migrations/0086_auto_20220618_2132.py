# Generated by Django 2.1.13 on 2022-06-19 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0085_auto_20220617_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestsection',
            name='request_section_source_id',
            field=models.ForeignKey(blank=True, db_column='RequestSectionSourceID', default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rrf.RequestSection'),
        ),
    ]