from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User,verbose_name='', on_delete=models.CASCADE,
                                related_name='client')
    organization = models.CharField(verbose_name='',max_length=200)
    inn = models.PositiveIntegerField(verbose_name='',)
    address = models.CharField(verbose_name='',max_length=200)
    okpo = models.PositiveIntegerField(verbose_name='',)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Driver(models.Model):
    user = models.OneToOneField(User, verbose_name='Водитель', on_delete=models.CASCADE,
                                related_name='driver')
    car_number = models.CharField(verbose_name='Номер машины', max_length=50)
    category = models.CharField(verbose_name='Категория',max_length=30)
    car_model = models.CharField(verbose_name='Модель',max_length=100)
    year_of_issue = models.PositiveIntegerField(verbose_name='Год выпуска',)
    color = models.CharField(verbose_name='Цвет',max_length=100)
    chassis = models.CharField(verbose_name='Шасси',max_length=100)
    body_type = models.CharField(verbose_name='Кузов',max_length=100)
    engine_power = models.CharField(verbose_name='Мощность двигателя',max_length=100)
    engine_type = models.CharField(verbose_name='Тип двигателя',max_length=100)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Order(models.Model):
    name = models.CharField(verbose_name='Наименование заказа',max_length=100)
    owner = models.ForeignKey(Client,verbose_name='Отправитель', on_delete=models.CASCADE,
                              related_name='orders')
    receiver = models.CharField(verbose_name='Получатель',max_length=200)
    invoice = models.FileField(verbose_name='Инвойс',upload_to='files/invoice')
    packing_list = models.FileField(verbose_name='Упаковочный лист',upload_to='files/packing_list')
    driver = models.ForeignKey(Driver,verbose_name='Водитель', on_delete=models.SET_NULL,
                               related_name='orders', null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Worker(models.Model):
    user = models.OneToOneField(User,verbose_name='Рабочий', on_delete=models.CASCADE,
                                related_name='worker')
    organization = models.CharField(verbose_name='Название организации',max_length=100)
    phone = models.CharField(verbose_name='Тел.номер',max_length=200)
    passport_id = models.PositiveIntegerField(verbose_name='ID паспорта',)
    place = models.CharField(verbose_name='Адрес',max_length=200)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'