# Generated by Django 2.1.13 on 2022-09-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0141_auto_20220907_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accrangetypehistory',
            name='tm_range_type_code',
            field=models.TextField(db_column='TMRangeTypeCode', default=None, max_length=10, null=True),
        ),
    ]
