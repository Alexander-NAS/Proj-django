# Generated by Django 4.2.6 on 2024-07-09 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_category_alter_products_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('id',), 'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
