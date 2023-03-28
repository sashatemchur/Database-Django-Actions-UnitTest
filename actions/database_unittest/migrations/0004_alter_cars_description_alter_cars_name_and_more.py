# Generated by Django 4.1.7 on 2023-03-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_unittest', '0003_alter_cars_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='name',
            field=models.CharField(max_length=75, verbose_name='Name car'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='owners',
            field=models.CharField(max_length=120, verbose_name='Owners'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='balance',
            field=models.FloatField(max_length=50, verbose_name='Balance'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name clients'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='reg_date',
            field=models.DateField(verbose_name='Register Date'),
        ),
        migrations.AlterField(
            model_name='voleybolteams',
            name='name',
            field=models.CharField(max_length=350, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='voleybolteams',
            name='power',
            field=models.CharField(max_length=25, verbose_name='Power'),
        ),
    ]