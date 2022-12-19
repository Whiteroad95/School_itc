from django.db import models


class Headmaster(models.Model):
    name_surname = models.CharField(max_length=255, verbose_name='ФИО')
    photo = models.ImageField(upload_to='photo', verbose_name='Фотография директора')
    number = models.CharField(max_length=255, verbose_name='Номер')

    def __str__(self):
        return self.name_surname


class Headteacher(models.Model):
    name_surname = models.CharField(max_length=255, verbose_name='ФИО')
    photo = models.ImageField(upload_to='photo', verbose_name='Фотография ')
    number = models.CharField(max_length=255, verbose_name='Номер')

    def __str__(self):
        return self.name_surname


class Teachers(models.Model):
    name_surname = models.CharField(max_length=255, verbose_name='ФИО')
    address = models.CharField(max_length=255, verbose_name='Место проживания')
    number = models.CharField(max_length=255, verbose_name='Номер')
    photo = models.ImageField(upload_to='photo', verbose_name='Фотография ')

    def __str__(self):
        return self.name_surname





# Create your models here.
