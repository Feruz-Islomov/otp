# Generated by Django 3.1.14 on 2023-01-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20230115_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
