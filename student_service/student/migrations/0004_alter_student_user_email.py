# Generated by Django 5.1 on 2025-04-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_coursematerial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
