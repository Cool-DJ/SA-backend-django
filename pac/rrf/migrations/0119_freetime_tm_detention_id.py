# Generated by Django 2.1.13 on 2022-08-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0118_auto_20220804_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='freetime',
            name='tm_detention_id',
            field=models.BigIntegerField(db_column='TMDetentionID', default=None, null=True),
        ),
    ]
