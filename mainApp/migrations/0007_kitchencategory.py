# Generated by Django 3.1.7 on 2021-04-05 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_fruits'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.fruits')),
                ('vegetables', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.vegetables')),
            ],
        ),
    ]
