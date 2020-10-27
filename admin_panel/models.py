from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='client')
    organization = models.CharField(max_length=200)
    inn = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    okpo = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


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

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Order(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE,
                              related_name='orders')
    receiver = models.CharField(max_length=200)
    invoice = models.FileField(upload_to='files/invoice')
    packing_list = models.FileField(upload_to='files/packing_list')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL,
                               related_name='orders', null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='worker')
    organization = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    passport_id = models.PositiveIntegerField()
    full_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'