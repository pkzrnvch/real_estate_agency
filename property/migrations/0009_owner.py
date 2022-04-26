# Generated by Django 2.2.24 on 2022-04-25 11:28

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20220425_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('pure_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализированный номер телефона')),
                ('flats_in_ownership', models.ManyToManyField(related_name='flat_owner', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]