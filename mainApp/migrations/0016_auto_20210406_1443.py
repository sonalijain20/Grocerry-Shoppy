# Generated by Django 3.1.7 on 2021-04-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0015_remove_buyer_ifsccode'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='accountNumber',
            field=models.CharField(blank=True, default=None, max_length=28, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='bankName',
            field=models.CharField(blank=True, default=None, max_length=28, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='ifscCode',
            field=models.CharField(blank=True, default=None, max_length=28, null=True),
        ),
    ]
