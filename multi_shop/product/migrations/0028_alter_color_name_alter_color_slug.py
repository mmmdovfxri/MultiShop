# Generated by Django 4.1.1 on 2022-11-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_alter_product_color_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
