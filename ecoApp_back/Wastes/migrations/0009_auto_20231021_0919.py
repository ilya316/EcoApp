# Generated by Django 3.2.21 on 2023-10-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wastes', '0008_auto_20230930_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wastesite',
            name='waste_type',
        ),
        migrations.AddField(
            model_name='wastesite',
            name='address',
            field=models.CharField(default=2, max_length=255, verbose_name='Addres'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wastesite',
            name='yard_type',
            field=models.CharField(default=2, max_length=100, verbose_name='Yard_type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wastetypes',
            name='yard_type',
            field=models.CharField(default=2, max_length=100, verbose_name='Yard type'),
            preserve_default=False,
        ),
    ]
