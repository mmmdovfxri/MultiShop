# Generated by Django 4.1.1 on 2022-10-07 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Signin',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]