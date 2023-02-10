from django.db import models

# Create your models here.


class SampleModel(models.Model):
    file = models.FileField()


class Kitchen(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    shipping_tax = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    open = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
