# Generated by Django 3.2.3 on 2021-06-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210611_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]
