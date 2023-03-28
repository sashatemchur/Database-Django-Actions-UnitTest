# Generated by Django 4.1.7 on 2023-03-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name car')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('price', models.FloatField(max_length=250, verbose_name='Price')),
                ('owners', models.IntegerField(max_length=250, verbose_name='Owners')),
                ('max_speed', models.IntegerField(max_length=250, verbose_name='Speed')),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name clients')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('status', models.BooleanField(max_length=250, verbose_name='Status')),
                ('balance', models.FloatField(max_length=250, verbose_name='Balance')),
                ('reg_date', models.DateField(max_length=250, verbose_name='Register Date')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
        ),
        migrations.CreateModel(
            name='VoleybolTeams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('speed', models.IntegerField(max_length=250, verbose_name='Speed')),
                ('price', models.FloatField(max_length=250, verbose_name='Price')),
                ('jump', models.FloatField(max_length=250, verbose_name='Jump')),
                ('power', models.CharField(max_length=250, verbose_name='Power')),
            ],
            options={
                'verbose_name': 'human',
                'verbose_name_plural': 'humans',
            },
        ),
    ]
