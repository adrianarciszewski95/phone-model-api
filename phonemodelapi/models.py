from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class PhoneImage(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='phone images')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField(null=True, blank=True, upload_to='brand logos')

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class OSVersion(models.Model):
    name = models.CharField(max_length=20)
    os = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.os.name} {self.name}"


class Chipset(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class QuickCharge(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(max_length=30)
    phone_images = models.ManyToManyField(PhoneImage)

    #general
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank=True)

    #body
    height = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    width = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    thickness = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)

    #display
    display_resolution_height = models.IntegerField(null=True, blank=True)
    display_resolution_width = models.IntegerField(null=True, blank=True)
    display_diagonal = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    DISPLAY_TECHNOLOGIES = [
        ('IP', 'IPS'),
        ('OL', 'OLED'),
    ]
    display_technology = models.CharField(choices=DISPLAY_TECHNOLOGIES, max_length=20)

    #platform
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    os_version = models.ForeignKey(OSVersion, on_delete=models.CASCADE)
    chipset = models.ForeignKey(Chipset, on_delete=models.CASCADE)
    processor_clock = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    processor_cores = models.IntegerField(null=True, blank=True)

    #memory
    internal_memory = models.IntegerField(null=True, blank=True)
    ram_memory = models.IntegerField(null=True, blank=True)
    memory_card_slot = models.BooleanField()

    #battery
    battery_capacity = models.IntegerField(null=True, blank=True)
    battery_removable = models.BooleanField()
    quick_battery_charging = models.ForeignKey(QuickCharge, on_delete=models.CASCADE)
    wireless_battery_charging = models.BooleanField()

    #camera
    back_camera_resolution = models.IntegerField(null=True, blank=True)
    back_camera_video = models.IntegerField(null=True, blank=True)
    back_camera_amount = models.IntegerField(null=True, blank=True)
    front_camera_resolution = models.IntegerField(null=True, blank=True)
    front_dual_camera = models.BooleanField()

    #sim
    SIM_SIZE = [
        ('MI', 'miniSIM'),
        ('MC', 'microSIM'),
        ('NS', 'nanoSIM')
    ]
    sim_size = models.CharField(choices=SIM_SIZE, max_length=20)
    dual_sim = models.BooleanField()
    e_sim = models.BooleanField()

    #other
    audio_jack = models.BooleanField()
    bluetooth_version = models.DecimalField(decimal_places=1, max_digits=3, null=True, blank=True)
    FINGERPRINT_TYPES = [
        ('NO', 'no'),
        ('FM', 'front-mounted'),
        ('RM', 'rear-mounted'),
        ('SM', 'side-mounted'),
        ('UD', 'under display')
    ]
    fingerprint = models.CharField(choices=FINGERPRINT_TYPES, max_length=20)
    nfc = models.BooleanField(verbose_name="NFC")
    USB_TYPES = [
        ('OT', 'other'),
        ('MI', 'microUSB'),
        ('TC', 'type C'),
        ('LG', 'lightning')

    ]
    usb_type = models.CharField(choices=USB_TYPES, max_length=20)
    additional_information = models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.name_with_brand()

    def name_with_brand(self):
        return f"{self.brand.name} {self.name}"

    def number_of_ratings(self):
        ratings = Rating.objects.filter(phone=self)
        return len(ratings)

    def average_rating(self):
        ratings = Rating.objects.filter(phone=self)
        sum = 0
        for rating in ratings:
            sum += rating.start
        number_of_ratings = self.number_of_ratings()
        return sum/number_of_ratings if number_of_ratings > 0 else 0


class Rating(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    opinion = models.TextField(null=True, blank=True, max_length=500)

    class Meta:
        unique_together = ['user', 'phone']
        index_together = ['user', 'phone']



