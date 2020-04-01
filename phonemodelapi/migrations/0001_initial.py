# Generated by Django 3.0.4 on 2020-03-21 20:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='brand logos')),
            ],
        ),
        migrations.CreateModel(
            name='Chipset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OSVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonemodelapi.OperatingSystem')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='phone images')),
            ],
        ),
        migrations.CreateModel(
            name='QuickCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('thickness', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('display_resolution_height', models.IntegerField(blank=True, null=True)),
                ('display_resolution_width', models.IntegerField(blank=True, null=True)),
                ('display_diagonal', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('display_technology', models.CharField(choices=[('IP', 'IPS'), ('OL', 'OLED')], max_length=20)),
                ('processor_clock', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('processor_cores', models.IntegerField(blank=True, null=True)),
                ('internal_memory', models.IntegerField(blank=True, null=True)),
                ('ram_memory', models.IntegerField(blank=True, null=True)),
                ('memory_card_slot', models.BooleanField()),
                ('battery_capacity', models.IntegerField(blank=True, null=True)),
                ('battery_removable', models.BooleanField()),
                ('wireless_battery_charging', models.BooleanField()),
                ('back_camera_resolution', models.IntegerField(blank=True, null=True)),
                ('back_camera_video', models.IntegerField(blank=True, null=True)),
                ('back_camera_amount', models.IntegerField(blank=True, null=True)),
                ('front_camera_resolution', models.IntegerField(blank=True, null=True)),
                ('front_dual_camera', models.BooleanField()),
                ('sim_size', models.CharField(choices=[('MI', 'miniSIM'), ('MC', 'microSIM'), ('NS', 'nanoSIM')], max_length=20)),
                ('dual_sim', models.BooleanField()),
                ('e_sim', models.BooleanField()),
                ('audio_jack', models.BooleanField()),
                ('bluetooth_version', models.DecimalField(decimal_places=1, default=5.0, max_digits=3)),
                ('fingerprint', models.CharField(choices=[('NO', 'no'), ('FM', 'front-mounted'), ('RM', 'rear-mounted'), ('SM', 'side-mounted'), ('UD', 'under display')], max_length=20)),
                ('nfc', models.BooleanField()),
                ('usb_type', models.CharField(choices=[('OT', 'other'), ('MI', 'microUSB'), ('TC', 'type C'), ('LG', 'lightning')], max_length=20)),
                ('additional_information', models.TextField(blank=True, max_length=500, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonemodelapi.Brand')),
                ('chipset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonemodelapi.Chipset')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phonemodelapi.Color')),
                ('operating_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonemodelapi.OperatingSystem')),
                ('os_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonemodelapi.OSVersion')),
                ('phone_images', models.ManyToManyField(to='phonemodelapi.PhoneImage')),
                ('quick_battery_charging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonemodelapi.QuickCharge')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('opinion', models.TextField(blank=True, max_length=500, null=True)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonemodelapi.Phone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'phone')},
                'index_together': {('user', 'phone')},
            },
        ),
    ]
