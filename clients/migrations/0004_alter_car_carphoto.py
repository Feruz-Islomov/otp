# Generated by Django 4.1.3 on 2022-11-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_car_carphoto_alter_car_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='carPhoto',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]