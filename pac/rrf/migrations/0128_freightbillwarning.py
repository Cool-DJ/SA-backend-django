# Generated by Django 2.1.13 on 2022-08-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0127_merge_20220811_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreightBillWarning',
            fields=[
                ('freight_bill_warning_id', models.BigAutoField(db_column='FreightBillsWarningID', primary_key=True, serialize=False)),
                ('freight_bill_number', models.CharField(db_column='FreightBillNo', max_length=50, null=True)),
                ('origin', models.TextField(db_column='Origin', default=None, max_length=50, null=True)),
                ('destination', models.TextField(db_column='Destination', default=None, max_length=50, null=True)),
                ('service_level', models.TextField(db_column='ServiceLevel', default=None, max_length=50, null=True)),
                ('billed_weight', models.DecimalField(db_column='BilledWeight', decimal_places=6, default=None, max_digits=19, null=True)),
                ('costing_date', models.DateField(db_column='CostingDate', max_length=50, null=True)),
                ('revenue', models.DecimalField(db_column='Revenue', decimal_places=6, default=None, max_digits=19, null=True)),
                ('total_cost', models.DecimalField(db_column='TotalCost', decimal_places=6, default=None, max_digits=19, null=True)),
                ('profit', models.DecimalField(db_column='Profit', decimal_places=6, default=None, max_digits=19, null=True)),
            ],
            options={
                'verbose_name_plural': 'FreightBillWarning',
                'db_table': 'FreightBillWarning',
            },
        ),
    ]
