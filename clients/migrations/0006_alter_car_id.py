# Generated by Django 4.1.3 on 2022-12-10 12:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_rename_carmodel_car_model_rename_carphoto_car_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
