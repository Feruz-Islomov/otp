# Generated by Django 3.1.14 on 2023-01-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0019_auto_20230101_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='latitude',
            field=models.IntegerField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='longitude',
            field=models.IntegerField(max_length=30, null=True),
        ),
    ]