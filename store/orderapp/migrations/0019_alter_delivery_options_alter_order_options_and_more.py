# Generated by Django 4.2.4 on 2023-08-21 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0018_remove_productorder_profileid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Доставка', 'verbose_name_plural': 'Доставки'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='productorder',
            options={'verbose_name': 'Товар заказа', 'verbose_name_plural': 'Товары заказов'},
        ),
    ]