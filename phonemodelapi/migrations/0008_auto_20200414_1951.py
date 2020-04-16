# Generated by Django 3.0.4 on 2020-04-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonemodelapi', '0007_auto_20200412_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='bluetooth_version',
            field=models.CharField(choices=[('unknown', 'unknown'), ('Bluetooth 1.0', 'Bluetooth 1.0'), ('Bluetooth 1.1', 'Bluetooth 1.1'), ('Bluetooth 1.2', 'Bluetooth 1.2'), ('Bluetooth 2.0', 'Bluetooth 2.0'), ('Bluetooth 2.1', 'Bluetooth 2.1'), ('Bluetooth 3.0', 'Bluetooth 3.0'), ('Bluetooth 3.1', 'Bluetooth 3.1'), ('Bluetooth 4.0', 'Bluetooth 4.0'), ('Bluetooth 4.1', 'Bluetooth 4.1'), ('Bluetooth 4.2', 'Bluetooth 4.2'), ('Bluetooth 5.0', 'Bluetooth 5.0')], default='null', max_length=20),
        ),
    ]