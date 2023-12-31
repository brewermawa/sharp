# Generated by Django 4.2.5 on 2023-11-15 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_menu_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=60, verbose_name='name')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator('[(]?[0-9]{2,3}[)]?[-\\s]?[0-9]{3,4}[-\\s]?[0-9]{4}$')])),
            ],
        ),
    ]
