# Generated by Django 5.0.1 on 2024-02-16 05:03

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_good_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='img',
            field=models.ImageField(default=1, upload_to=main.models.good_directory_path),
            preserve_default=False,
        ),
    ]
