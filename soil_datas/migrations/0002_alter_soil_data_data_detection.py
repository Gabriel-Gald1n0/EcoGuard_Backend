# Generated by Django 5.1.2 on 2024-12-08 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_detections', '0001_initial'),
        ('soil_datas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soil_data',
            name='data_detection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_detections.data_detection'),
        ),
    ]