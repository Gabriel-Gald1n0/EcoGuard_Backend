# Generated by Django 5.1.2 on 2024-10-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0003_alter_region_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='street',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]