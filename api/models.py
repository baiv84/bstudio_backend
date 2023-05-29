from django.db import models
from django.utils import timezone


class Service(models.Model):
    """Beauty Studio services implementation"""
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        """Object <Service> string representation"""
        return self.name


class Master(models.Model):
    """Beauty Studio employer (master) implementation"""
    name = models.CharField(max_length=100)
    services = models.ManyToManyField('Service',
                                      verbose_name='Оказываемые услуги',
                                      related_name='masters')

    def __str__(self):
        """Object <Master> string representation"""
        return self.name


class Client(models.Model):
    """Beauty Studio clients implementation"""
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        """Object <Client> string representation"""
        return self.name


class Appointment(models.Model):
    """Object <Appointment> string representation"""
    client = models.ForeignKey(Client,
                               verbose_name='Имя клиента',
                               on_delete=models.CASCADE,
                               related_name='appointments')
    service = models.ForeignKey(Service,
                                verbose_name='Оказанная услуга',
                                on_delete=models.CASCADE,
                                related_name='appointments')
    master = models.ForeignKey(Master,
                               verbose_name='Мастер',
                               on_delete=models.CASCADE,
                               related_name='appointments')
    appointment_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Object <Appointment> string representation"""
        return f'{self.client} ordered {self.service} \
              at {self.appointment_datetime}, master - {self.master}'
