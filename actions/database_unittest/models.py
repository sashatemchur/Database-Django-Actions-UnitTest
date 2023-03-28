from django.db import models


class Clients(models.Model):
    name = models.CharField('Name clients', max_length=250)
    description = models.CharField('Description', max_length=250)
    status = models.BooleanField('Status')
    balance = models.FloatField('Balance', max_length=250)
    reg_date = models.DateField('Register Date', max_length=250)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "client"
        verbose_name_plural= "clients"


class Cars(models.Model):
    name = models.CharField('Name car', max_length=250)
    description = models.CharField('Description', max_length=250)
    price = models.FloatField('Price')
    owners = models.IntegerField('Owners')
    max_speed = models.IntegerField('Speed')

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "car"
        verbose_name_plural= "cars"


class VoleybolTeams(models.Model):
    name = models.CharField('Name', max_length=250)
    speed = models.IntegerField('Speed')
    price = models.FloatField('Price')
    jump = models.FloatField('Jump')
    power = models.CharField('Power', max_length=250)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "human"
        verbose_name_plural= "humans"