# Generated by Django 3.1.7 on 2021-04-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20210405_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='beverages',
            name='img1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='beverages',
            name='l1',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
