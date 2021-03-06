# Generated by Django 3.1.7 on 2021-04-15 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0027_cart_finalprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('name', models.CharField(default=None, max_length=20)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('email', models.CharField(default=None, max_length=20)),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('notes', models.TextField(default=None)),
                ('pin', models.CharField(max_length=20)),
                ('mode', models.CharField(default=None, max_length=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
    ]
