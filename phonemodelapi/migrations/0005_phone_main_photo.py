# Generated by Django 3.0.4 on 2020-04-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonemodelapi', '0004_auto_20200408_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to='phone images'),
        ),
    ]