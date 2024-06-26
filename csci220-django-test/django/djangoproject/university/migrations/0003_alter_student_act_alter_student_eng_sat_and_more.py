# Generated by Django 4.2.11 on 2024-04-25 00:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_alter_participates_in_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ACT',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(36)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='eng_SAT',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(200), django.core.validators.MaxValueValidator(800)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='math_SAT',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(200), django.core.validators.MaxValueValidator(800)]),
        ),
    ]
