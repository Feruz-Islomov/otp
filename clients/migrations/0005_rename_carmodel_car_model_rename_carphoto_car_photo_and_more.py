# Generated by Django 4.1.3 on 2022-12-04 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_car_carphoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='carModel',
            new_name='Model',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='carPhoto',
            new_name='Photo',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='carColor',
            new_name='Rang',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='carNumber',
            new_name='Raqam',
        ),
    ]
