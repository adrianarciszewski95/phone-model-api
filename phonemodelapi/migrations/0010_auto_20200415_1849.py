# Generated by Django 3.0.4 on 2020-04-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonemodelapi', '0009_auto_20200414_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='average_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='number_of_ratings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
