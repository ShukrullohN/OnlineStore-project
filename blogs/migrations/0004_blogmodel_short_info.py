# Generated by Django 5.0.4 on 2024-05-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogtagmodel_blogmodel_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='short_info',
            field=models.TextField(null=True),
        ),
    ]
