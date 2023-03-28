from django.contrib import admin
from .models import Clients, Cars, VoleybolTeams 


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    ...


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    ...


@admin.register(VoleybolTeams)
class VoleybolTeamsAdmin(admin.ModelAdmin):
    ...
