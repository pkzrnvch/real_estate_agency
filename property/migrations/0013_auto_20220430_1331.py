# Generated by Django 2.2.24 on 2022-04-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220428_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats_in_ownership',
            field=models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
