# Generated by Django 4.0.5 on 2022-06-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wcity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='price',
            field=models.BigIntegerField(default=0),
        ),
    ]