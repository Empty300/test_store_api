# Generated by Django 4.1.5 on 2023-01-18 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('specifications', models.TextField(blank=True, verbose_name='Характеристики')),
                ('price_now', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True, verbose_name='Текущая цена')),
                ('price_old', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Предыдущая цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество на складе')),
                ('image1', models.URLField(max_length=256, null=True)),
                ('image2', models.URLField(max_length=256, null=True)),
                ('image3', models.URLField(max_length=256, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('short_description', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
                ('colors', models.CharField(blank=True, max_length=100, verbose_name='Цвета')),
                ('discount', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True, verbose_name='Скидка')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='Бренд')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('products_count', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Количество товара')),
                ('image1', models.URLField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=1000, verbose_name='Отзыв')),
                ('stars', models.PositiveSmallIntegerField(verbose_name='Оценка')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
        ),
    ]
