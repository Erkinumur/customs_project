from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='client')
    organization = models.CharField(max_length=200)
    inn = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    okpo = models.PositiveIntegerField()


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='driver')
    car_number = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    car_model = models.CharField(max_length=100)
    year_of_issue = models.PositiveIntegerField()
    colour = models.CharField(max_length=100)
    chassis = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    engine_power = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)


class Order(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE,
                              related_name='orders')
    receiver = models.CharField(max_length=200)
    invoice = models.FileField(upload_to='files')
    packing_list = models.FileField(upload_to='files')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL,
                               related_name='orders', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('client_order', args=[str(self.pk)])


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='worker')
    organization = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    passport_id = models.PositiveIntegerField()
    full_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)