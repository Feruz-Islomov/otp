# Generated by Django 3.1.14 on 2023-01-02 15:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0019_auto_20230101_1546'),
        ('washers', '0004_ishchi'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ishchi',
            new_name='Driver_cart_order',
        ),
    ]
