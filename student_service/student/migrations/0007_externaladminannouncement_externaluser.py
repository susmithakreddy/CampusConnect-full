# Generated by Django 5.1 on 2025-04-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_remove_submission_file_url_submission_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalAdminAnnouncement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('target_type', models.CharField(max_length=20)),
                ('target_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'admin_adminannouncement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExternalUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'users_user',
                'managed': False,
            },
        ),
    ]
