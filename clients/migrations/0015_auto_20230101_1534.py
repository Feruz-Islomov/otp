# Generated by Django 3.1.14 on 2023-01-01 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0014_auto_20230101_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('cost', models.CharField(max_length=30, null=True)),
                ('part', models.CharField(max_length=50, null=True)),
                ('paytype', models.CharField(max_length=20, null=True)),
                ('latitude', models.CharField(max_length=30, null=True)),
                ('longitude', models.CharField(max_length=30, null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.car')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
