from django.db import models

# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Holiday(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=128)
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE, null=True, blank=True)
    season = models.ForeignKey(to=Season, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    is_available = models.BooleanField()
    image = models.ImageField(upload_to='products_images')
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    holiday = models.ForeignKey(to=Holiday, on_delete=models.CASCADE, null=True, blank=True)
    main_flower = models.ForeignKey(to=Flower, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

