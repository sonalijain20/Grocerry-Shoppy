# Generated by Django 3.1.7 on 2021-04-15 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0031_auto_20210415_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.cart'),
        ),
    ]
