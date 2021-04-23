from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    seats = models.IntegerField(default=4)
    color = models.CharField(max_length=128)
    vin = models.CharField("VIN", max_length=17)
    current_mileage = models.IntegerField(default=0)
    service_interval = models.CharField(max_length=128)
    next_service = models.DateField()

    def __str__(self):
        return '%s %s %s' % (self.make, self.model, self.year)

class Truck(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    seats = models.IntegerField()
    bed_length = models.CharField(max_length=64)
    color = models.CharField(max_length=128)
    vin = models.CharField("VIN", max_length=17)
    current_mileage = models.IntegerField(default=0)
    service_interval = models.CharField(max_length=128)
    next_service = models.DateField()

    def __str__(self):
        return '%s %s %s' % (self.make, self.model, self.year)

class Boat(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    length = models.CharField(max_length=64)
    width = models.CharField(max_length=64)
    hin = models.CharField("HIN", max_length=12)
    current_hours = models.IntegerField()
    service_interval = models.CharField(max_length=128)
    next_service = models.DateField()

    def __str__(self):
        return '%s %s %s' % (self.make, self.model, self.year)
