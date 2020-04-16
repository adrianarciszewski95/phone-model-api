# Generated by Django 3.0.4 on 2020-04-12 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phonemodelapi', '0006_auto_20200412_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='phonemodelapi.Brand'),
        ),
    ]
