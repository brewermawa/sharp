# Generated by Django 4.2.5 on 2023-11-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='image',
            field=models.ImageField(blank=True, help_text='Promo image', null=True, upload_to='promo', verbose_name='Image file'),
        ),
    ]
