# Generated by Django 5.1.2 on 2024-12-08 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_report_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
    ]
