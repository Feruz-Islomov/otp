# Generated by Django 3.1.14 on 2023-01-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_auto_20230101_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
