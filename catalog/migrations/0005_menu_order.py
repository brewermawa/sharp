# Generated by Django 4.2.5 on 2023-11-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_brand_product_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
