# Generated by Django 4.1.2 on 2022-11-05 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_login_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]