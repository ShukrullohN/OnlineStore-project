# Generated by Django 5.0.4 on 2024-05-30 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productmodel_discount_productimagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='discount',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='discount_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]