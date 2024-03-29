# Generated by Django 5.0 on 2024-01-03 01:41

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.CharField(help_text='Announcement text', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Brand name', max_length=60, unique=True, verbose_name='name')),
                ('slug', models.SlugField(help_text='Friendly URl slug', max_length=60, unique=True)),
                ('logo', models.ImageField(help_text='Brand logo', upload_to='brand', verbose_name='Brand logo')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Business Name (Razón Social)', max_length=60, verbose_name='Razón social')),
                ('street', models.CharField(help_text='Street', max_length=60, verbose_name='Calle')),
                ('ext_number', models.CharField(help_text='External number', max_length=10, verbose_name='Número exterior')),
                ('int_number', models.CharField(help_text='Internal number', max_length=10, verbose_name='Número interior')),
                ('neighbourhood', models.CharField(help_text='Colonia', max_length=60, verbose_name='Colonia')),
                ('city', models.CharField(help_text='Munucipio', max_length=60, verbose_name='Municipio')),
                ('state', models.CharField(help_text='Estado', max_length=60, verbose_name='Estado')),
                ('zip_code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[0-9]{5}$')])),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator('[(]?[0-9]{2,3}[)]?[-\\s]?[0-9]{3,4}[-\\s]?[0-9]{4}$')])),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'Business Info',
                'verbose_name_plural': 'Business Info',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator('[(]?[0-9]{2,3}[)]?[-\\s]?[0-9]{3,4}[-\\s]?[0-9]{4}$')])),
                ('message', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Feauture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Feauture name', max_length=60, unique=True, verbose_name='Feauture name')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category name', max_length=60, unique=True, verbose_name='name')),
                ('slug', models.SlugField(help_text='Friendly URl slug', max_length=60, unique=True)),
                ('short_description', models.TextField(verbose_name='Short description')),
                ('large_description', models.TextField(verbose_name='Large description')),
                ('image', models.ImageField(blank=True, help_text='Category image', null=True, upload_to='category', verbose_name='Image')),
                ('thumbnail', models.ImageField(blank=True, help_text='Category thumbnail image', null=True, upload_to='category/thumbnail', verbose_name='Thumbnail image')),
                ('created_date', models.DateField(auto_now_add=True, help_text='Creation date', null=True)),
                ('modified_date', models.DateField(auto_now_add=True, help_text='Modified date', null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_categories', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_categories', to=settings.AUTH_USER_MODEL)),
                ('parent_category', models.ForeignKey(blank=True, help_text='The parent category', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_categories', to='catalog.category', verbose_name='Parent category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filterType', models.CharField(choices=[('sel', 'Dropdown'), ('rad', 'Radio button'), ('chk', 'Checkboxes'), ('rng', 'Range'), ('txt', 'Text')], default='sel', max_length=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='catalog.category')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.feauture')),
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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Product name', max_length=60, unique=True, verbose_name='name')),
                ('slug', models.SlugField(help_text='Friendly URL slug', max_length=60, unique=True)),
                ('sku', models.CharField(help_text='Stock keeping unit', max_length=15, unique=True, verbose_name='SKU')),
                ('upc', models.CharField(help_text='Universal product code', max_length=12, unique=True, verbose_name='UPC')),
                ('short_description', models.TextField(verbose_name='Short description')),
                ('large_Description', models.TextField(verbose_name='Large description')),
                ('created_date', models.DateField(auto_now_add=True, help_text='Creation date', null=True)),
                ('modified_date', models.DateField(auto_now_add=True, help_text='Modified date', null=True)),
                ('active', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brand', models.ForeignKey(help_text='The brand or manufacturer of the product', on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalog.brand')),
                ('categories', models.ManyToManyField(help_text='Other categories where the product should be shown', to='catalog.category')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_product', to=settings.AUTH_USER_MODEL)),
                ('main_category', models.ForeignKey(help_text='The parent category of the product', on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalog.category', verbose_name='Parent category')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_product', to=settings.AUTH_USER_MODEL)),
                ('related_product', models.ManyToManyField(blank=True, help_text='Related products', related_name='related', to='catalog.product', verbose_name='Related products')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('url', models.CharField(blank=True, max_length=30, null=True)),
                ('order', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
            },
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
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Image name', max_length=60, unique=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, help_text='Product image', null=True, upload_to='product/', verbose_name='Product image file')),
                ('main', models.BooleanField(default=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Pricing name', max_length=60, unique=True, verbose_name='Name')),
                ('discount_type', models.CharField(choices=[('p', 'Percentage'), ('d', 'Direct')], default='p', max_length=1)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('active', models.BooleanField(default=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pricing', to='catalog.product')),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Promo title', max_length=60, unique=True, verbose_name='Title')),
                ('name', models.CharField(help_text='Promo name', max_length=60, unique=True, verbose_name='Name')),
                ('message', models.CharField(help_text='Promo message', max_length=60, unique=True, verbose_name='Message')),
                ('image', models.ImageField(blank=True, help_text='Promo image', null=True, upload_to='promo', verbose_name='Image file')),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promo', to='catalog.category')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promo', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Promo',
                'verbose_name_plural': 'Promos',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Slider title', max_length=60, unique=True, verbose_name='Title')),
                ('name', models.CharField(help_text='Slider name', max_length=60, unique=True, verbose_name='Name')),
                ('message', models.CharField(help_text='Slider message', max_length=60, unique=True, verbose_name='Message')),
                ('image', models.ImageField(blank=True, help_text='Slider image', null=True, upload_to='slider', verbose_name='Image file')),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slider', to='catalog.category')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slider', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.AddConstraint(
            model_name='productfeauturevalue',
            constraint=models.UniqueConstraint(fields=('product', 'feauture'), name='unique_product_feauture'),
        ),
    ]
