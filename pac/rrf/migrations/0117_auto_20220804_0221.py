# Generated by Django 2.1.13 on 2022-08-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0116_auto_20220804_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='revision_number',
            field=models.IntegerField(db_column='RevisionNumber', default=1),
        ),
        migrations.AddField(
            model_name='tariff',
            name='tariff_number',
            field=models.TextField(db_column='TariffNumber', default='_', max_length=30),
        ),
        migrations.AddField(
            model_name='tariffhistory',
            name='revision_number',
            field=models.IntegerField(db_column='RevisionNumber', default=1),
        ),
        migrations.AddField(
            model_name='tariffhistory',
            name='tariff_number',
            field=models.TextField(db_column='TariffNumber', default='_', max_length=30),
        ),
        migrations.AlterIndexTogether(
            name='tariff',
            index_together={('tariff_id', 'revision_number')},
        ),
    ]
