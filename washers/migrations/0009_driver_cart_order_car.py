# Generated by Django 3.1.14 on 2023-01-04 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0022_auto_20230104_1809'),
        ('washers', '0008_auto_20230104_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_cart_order',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.car'),
        ),
    ]
