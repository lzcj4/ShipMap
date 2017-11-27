from django.db import models


# Car models


class CarBrand(models.Model):
    name = models.CharField(max_length=100, verbose_name='car name', unique=True)
    index_char = models.CharField(max_length=10, blank=True, verbose_name='for quick location')


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100, verbose_name='car model name')


class CarFeature(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    market_year = models.IntegerField(verbose_name='model create year', default=0)
    front = models.CharField(max_length=100, verbose_name='front feature', blank=True)
    front_photo = models.CharField(max_length=100, verbose_name='front photo', blank=True)
    back = models.CharField(max_length=100, verbose_name='back feature', blank=True)
    back_photo = models.CharField(max_length=100, verbose_name='back photo', blank=True)
