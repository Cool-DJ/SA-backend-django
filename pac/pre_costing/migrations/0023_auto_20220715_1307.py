# Generated by Django 2.1.13 on 2022-07-15 13:07

from django.db import migrations, models, connection
import django.utils.timezone

# Method to add default datetime values for 
def alter_spotquote_updateon_default(apps, schema_editor):
  cursor_count = connection.cursor()
  sql_count = """
  SELECT COUNT(1) FROM sys.default_constraints dc
  INNER JOIN sys.objects o on o.object_id = dc.object_id
  WHERE o.name = 'DF_SpotQuoteMargin_UpdatedOn';
  """
  cursor_count.execute(sql_count)
  (const_result,)=cursor_count.fetchone()
  
  if (const_result <= 0):
    cursor_update = connection.cursor()
    sql_insert = """ALTER TABLE SpotQuoteMargin ADD CONSTRAINT DF_SpotQuoteMargin_UpdatedOn DEFAULT GETDATE() FOR UpdatedOn"""
    cursor_update.execute(sql_insert)

class Migration(migrations.Migration):

    dependencies = [
        ('pre_costing', '0022_auto_20220510_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotquotemargin',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, db_column='UpdatedOn', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spotquotemarginhistory',
            name='updated_on',
            field=models.DateTimeField(db_column='UpdatedOn', default=None),
        ),
        migrations.RunPython(alter_spotquote_updateon_default),
    ]
