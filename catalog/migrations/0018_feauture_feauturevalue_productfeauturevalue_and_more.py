# Generated by Django 4.2.5 on 2023-12-05 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_remove_productprice_discount_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feauture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Feauture name', max_length=60, unique=True, verbose_name='Feauture name')),
            ],
        ),
        migrations.CreateModel(
            name='FeautureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='Feauture value', max_length=25, verbose_name='Feauture value')),
                ('feauture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='catalog.feauture')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeautureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feauture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.feauture')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feautures', to='catalog.product')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.feauturevalue')),
            ],
        ),
        migrations.AddConstraint(
            model_name='productfeauturevalue',
            constraint=models.UniqueConstraint(fields=('product', 'feauture'), name='unique_product_feauture'),
        ),
    ]
