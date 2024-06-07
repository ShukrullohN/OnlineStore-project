# Generated by Django 5.0.4 on 2024-06-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_rename_catigories_blogmodel_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authormodel',
            name='about',
            field=models.TextField(verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='position',
            field=models.CharField(max_length=128, verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='profession',
            field=models.CharField(max_length=128, verbose_name='profession'),
        ),
        migrations.AlterField(
            model_name='blogcategorymodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='short_info',
            field=models.TextField(null=True, verbose_name='short_info'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='blogtagmodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
    ]
