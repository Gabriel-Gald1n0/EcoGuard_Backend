# Generated by Django 5.1.2 on 2024-10-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='message',
            field=models.TextField(),
        ),
    ]
