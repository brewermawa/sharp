# Generated by Django 4.2.5 on 2023-12-18 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_alter_productprice_final_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]