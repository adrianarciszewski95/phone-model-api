# Generated by Django 3.0.4 on 2020-04-17 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phonemodelapi', '0013_rating_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='phonemodelapi.Phone'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='phonemodelapi.Profile'),
        ),
    ]
