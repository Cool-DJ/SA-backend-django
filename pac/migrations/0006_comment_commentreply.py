# Generated by Django 2.1.13 on 2020-10-19 16:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0005_stored_procedures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('entity_uuid', models.CharField(db_column='EntityId', max_length=36)),
                ('entity_version', models.IntegerField(db_column='EntityVersion')),
                ('tag', models.CharField(db_column='Tag', max_length=100, null=True)),
                ('status', models.CharField(db_column='Status', default='ACTIVE', max_length=25, null=True)),
                ('type', models.CharField(db_column='Type', max_length=25, null=True)),
                ('content', models.TextField(db_column='Content')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='CreatedOn')),
                ('created_by', models.CharField(db_column='CreatedBy', max_length=100, null=True)),
                ('attachments', models.TextField(db_column='Attachments', default='[]')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('status', models.CharField(db_column='Status', default='ACTIVE', max_length=25, null=True)),
                ('content', models.TextField(db_column='Content')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='CreatedOn')),
                ('created_by', models.CharField(db_column='CreatedBy', max_length=100, null=True)),
                ('attachments', models.TextField(db_column='Attachments', default='[]')),
                ('comment', models.ForeignKey(db_column='Comment', on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='pac.Comment')),
            ],
            options={
                'db_table': 'CommentReply',
            },
        ),
    ]