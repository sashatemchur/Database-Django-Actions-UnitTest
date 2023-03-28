from django.test import TestCase
from .models import Clients, Cars, VoleybolTeams

class YourTestClass(TestCase):

    @classmethod
    def setUp(self):
        Clients.objects.create(name="Sasha", description="good programer kjsfhkdfhljkshdf", status=True, balance=4532.43, reg_date='2020-02-21')
        Cars.objects.create(name='BMW', description='good cars very beatufil sklhdkjgsfjh', price=12311313.43, owners='Sasha', max_speed=250)
        VoleybolTeams.objects.create(name='Denis', speed=15, price=1212.32, jump=265, power='34 km/h')


    def test_clients(self):
        clients = Clients.objects.get(id=1)
        expected_object_name = '%s' % (clients.name)
        self.assertEquals(expected_object_name, str(clients))


    def test_cars(self):
        cars = Cars.objects.get(id=1)
        expected_object_name = '%s, %s' % (cars.name, cars.owners)
        self.assertEquals(expected_object_name, str(cars))


    def test_voleybol_teams(self):
        team = VoleybolTeams.objects.get(id=1)
        expected_object_name = '%s' % (team.name)
        self.assertEquals(expected_object_name, str(team))


    def test_clients_name(self):
        clients = Clients.objects.get(id=1)
        max_length = clients._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


    def test_clients_description(self):
        clients = Clients.objects.get(id=1)
        max_length = clients._meta.get_field('description').max_length
        self.assertEquals(max_length, 250)


    def test_clients_balance(self):
        clients = Clients.objects.get(id=1)
        max_length = clients._meta.get_field('balance').max_length
        self.assertEquals(max_length, 50)


    def test_cars_name(self):
        cars = Cars.objects.get(id=1)
        max_length = cars._meta.get_field('name').max_length
        self.assertEquals(max_length, 75)


    def test_cars_description(self):
        cars = Cars.objects.get(id=1)
        max_length = cars._meta.get_field('description').max_length
        self.assertEquals(max_length, 300)


    def test_cars_owners(self):
        cars = Cars.objects.get(id=1)
        max_length = cars._meta.get_field('owners').max_length
        self.assertEquals(max_length, 120)


    def test_team_name(self):
        team = VoleybolTeams.objects.get(id=1)
        max_length = team._meta.get_field('name').max_length
        self.assertEquals(max_length, 350)


    def test_team_description(self):
        team = VoleybolTeams.objects.get(id=1)
        max_length = team._meta.get_field('power').max_length
        self.assertEquals(max_length, 25)
