# Generated by Django 4.1.1 on 2022-10-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_new_price_alter_size_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
