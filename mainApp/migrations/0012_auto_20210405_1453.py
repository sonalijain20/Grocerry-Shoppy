# Generated by Django 3.1.7 on 2021-04-05 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_auto_20210405_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beverages',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='quantity',
        ),
    ]
