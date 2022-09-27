# Generated by Django 2.1.13 on 2022-08-04 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0114_requestsectionhistory_request_version_id'),
    ]

    operations = [
#         migrations.AlterIndexTogether(
#             name='requestlanehistory',
#             index_together=set(),
#         ),
        migrations.RemoveField(
            model_name='requestlanehistory',
            name='request_lane',
        ),
        migrations.DeleteModel(
            name='RequestSectionLaneStaging',
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_number',
        ),
        migrations.RemoveField(
            model_name='requesthistory',
            name='request_number',
        ),
        migrations.RemoveField(
            model_name='requestsection',
            name='request_lane',
        ),
        migrations.RemoveField(
            model_name='requestsectionhistory',
            name='request_lane_version',
        ),
        migrations.DeleteModel(
            name='RequestLaneHistory',
        ),
        migrations.DeleteModel(
            name='RequestLane',
        ),
    ]
