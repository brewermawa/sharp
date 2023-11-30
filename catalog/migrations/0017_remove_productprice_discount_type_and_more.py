# Generated by Django 4.2.5 on 2023-11-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_productimages_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productprice',
            name='Discount type',
        ),
        migrations.AddField(
            model_name='productprice',
            name='discount_type',
            field=models.CharField(choices=[('p', 'Percentage'), ('d', 'Direct')], default='p', max_length=1),
        ),
    ]
