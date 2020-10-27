from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='client')
    full_name = models.CharField(max_length=200)


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='driver')
    full_name = models.CharField(max_length=200)
    car = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20)


class Order(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE,
                              related_name='orders')
    weight = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL,
                               related_name='orders', null=True, blank=True)
    status = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('client_order', args=[str(self.pk)])


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='worker')
    full_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)

