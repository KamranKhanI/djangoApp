# Generated by Django 2.1.2 on 2018-11-07 22:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mobile', '0003_auto_20181108_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='condition',
            field=models.PositiveSmallIntegerField(max_length=25, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10)]),
        ),
    ]