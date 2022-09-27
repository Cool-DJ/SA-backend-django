# Generated by Django 2.1.13 on 2022-07-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0019_auto_20220705_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='extended_payment_days',
            field=models.IntegerField(db_column='ExtendedPaymentDays', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='extended_payment_days_erp',
            field=models.IntegerField(db_column='ExtendedPaymentDays_ERP', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='extended_payment_terms_margin',
            field=models.FloatField(db_column='ExtendedPaymentTermsMargin', default=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='is_extended_payment',
            field=models.BooleanField(db_column='IsExtendedPayment', default=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='is_extended_payment_erp',
            field=models.BooleanField(db_column='IsExtendedPayment_ERP', default=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='is_paying_by_credit_card',
            field=models.BooleanField(db_column='IsPayingByCreditCard', default=True, null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='extended_payment_days',
            field=models.IntegerField(db_column='ExtendedPaymentDays', null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='extended_payment_days_erp',
            field=models.IntegerField(db_column='ExtendedPaymentDays_ERP', null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='extended_payment_terms_margin',
            field=models.FloatField(db_column='ExtendedPaymentTermsMargin', default=True, null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='is_extended_payment',
            field=models.BooleanField(db_column='IsExtendedPayment', default=True, null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='is_extended_payment_erp',
            field=models.BooleanField(db_column='IsExtendedPayment_ERP', default=True, null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='is_paying_by_credit_card',
            field=models.BooleanField(db_column='IsPayingByCreditCard', default=True, null=True),
        ),
    ]
