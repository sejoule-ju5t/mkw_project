# Generated by Django 2.0.6 on 2018-06-27 17:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tosca', '0002_auto_20180627_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='range',
            name='lower_bound',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='range',
            name='upper_bound',
            field=models.IntegerField(default=10000000000000),
        ),
        migrations.AddField(
            model_name='scalar-unit',
            name='scalar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scalar-unit',
            name='unit',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='state',
            name='transitional',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='state',
            name='value',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='version',
            name='build_version',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='version',
            name='fixed_version',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='version',
            name='major_version',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='version',
            name='minor_version',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='version',
            name='qualifier',
            field=models.CharField(max_length=100, null=True),
        ),
    ]