# Generated by Django 3.0.8 on 2020-09-11 07:12

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200911_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
