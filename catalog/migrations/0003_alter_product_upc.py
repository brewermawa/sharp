# Generated by Django 5.0 on 2024-01-09 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_upc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='upc',
            field=models.CharField(blank=True, help_text='Universal product code', max_length=12, verbose_name='UPC'),
        ),
    ]
