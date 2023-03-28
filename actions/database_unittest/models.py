from django.db import models


class Clients(models.Model):
    name = models.CharField('Name clients', max_length=100)
    description = models.CharField('Description', max_length=250)
    status = models.BooleanField('Status')
    balance = models.FloatField('Balance', max_length=50)
    reg_date = models.DateField('Register Date')

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "client"
        verbose_name_plural= "clients"


class Cars(models.Model):
    name = models.CharField('Name car', max_length=75)
    description = models.CharField('Description', max_length=300)
    price = models.FloatField('Price')
    owners = models.CharField('Owners', max_length=120)
    max_speed = models.IntegerField('Speed')

    
    def __str__(self):
        return '%s, %s' % (self.name, self.owners)

    class Meta:
        verbose_name = "car"
        verbose_name_plural= "cars"


class VoleybolTeams(models.Model):
    name = models.CharField('Name', max_length=350)
    speed = models.IntegerField('Speed')
    price = models.FloatField('Price')
    jump = models.FloatField('Jump')
    power = models.CharField('Power', max_length=25)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "human"
        verbose_name_plural= "humans"