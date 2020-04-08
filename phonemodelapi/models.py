from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class PhoneImage(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='phone images')


class Brand(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField(null=True, blank=True, upload_to='brand logos')

    def __str__(self):
        return self.name

    def number_of_phones(self):
        phones = Phone.objects.filter(brand=self)
        return len(phones)


class OperatingSystem(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(max_length=30)
    main_photo = models.ImageField(null=True, blank=True, upload_to='phone images')
    phone_images = models.ManyToManyField(PhoneImage)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank=True)
    display_diagonal = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    processor_clock = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    processor_cores = models.IntegerField(null=True, blank=True)
    internal_memory = models.IntegerField(null=True, blank=True)
    ram_memory = models.IntegerField(null=True, blank=True)
    memory_card_slot = models.BooleanField()
    battery_capacity = models.IntegerField(null=True, blank=True)
    battery_removable = models.BooleanField()
    quick_battery_charging = models.BooleanField()
    wireless_battery_charging = models.BooleanField()
    back_camera_resolution = models.IntegerField(null=True, blank=True)
    back_camera_amount = models.IntegerField(null=True, blank=True)
    front_camera_resolution = models.IntegerField(null=True, blank=True)
    SIM_SIZE = [
        ('miniSIM', 'miniSIM'),
        ('microSIM', 'microSIM'),
        ('NanoSIM', 'nanoSIM')
    ]
    sim_size = models.CharField(choices=SIM_SIZE, max_length=20)
    dual_sim = models.BooleanField()
    e_sim = models.BooleanField()
    audio_jack = models.BooleanField()
    bluetooth_version = models.DecimalField(decimal_places=1, max_digits=3, null=True, blank=True)
    FINGERPRINT_TYPES = [
        ('no', 'no'),
        ('front-mounted', 'front-mounted'),
        ('rear-mounted', 'rear-mounted'),
        ('side-mounted', 'side-mounted'),
        ('under display', 'under display')
    ]
    fingerprint = models.CharField(choices=FINGERPRINT_TYPES, max_length=20)
    nfc = models.BooleanField(verbose_name="NFC")
    USB_TYPES = [
        ('other', 'other'),
        ('microUSB', 'microUSB'),
        ('type C', 'type C'),
        ('lightning', 'lightning')

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



