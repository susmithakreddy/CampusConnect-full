# Generated by Django 5.1 on 2025-04-12 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0005_externaladminannouncement_delete_timetableentry'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='externaladminannouncement',
            table='admins_adminannouncement',
        ),
    ]
