# Generated by Django 3.1.7 on 2021-04-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0018_spices_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bakery',
            name='gm100',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='gm100_quan',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='gm250',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='gm250_quan',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='gm500',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='gm500_quan',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='kg1',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='kg1_quan',
        ),
        migrations.RemoveField(
            model_name='beverages',
            name='l1',
        ),
        migrations.RemoveField(
            model_name='beverages',
            name='l100',
        ),
        migrations.RemoveField(
            model_name='beverages',
            name='l100_quan',
        ),
        migrations.RemoveField(
            model_name='beverages',
            name='l1_quan',
        ),
        migrations.RemoveField(
            model_name='beverages',
            name='l250',
        ),
        migrations.RemoveField(
            model_name='beverages',
            name='l250_quan',
        ),
        migrations.RemoveField(
            model_name='beverages',
            name='l500',
        ),
        migrations.RemoveField(
            model_name='beverages',
            name='l500_quan',
        ),
        migrations.RemoveField(
            model_name='frozenfoods',
            name='gm100',
        ),
        migrations.RemoveField(
            model_name='frozenfoods',
            name='gm100_quan',
        ),
        migrations.RemoveField(
            model_name='frozenfoods',
            name='gm250',
        ),
        migrations.RemoveField(
            model_name='frozenfoods',
            name='gm250_quan',
        ),
        migrations.RemoveField(
            model_name='frozenfoods',
            name='gm500',
        ),
        migrations.RemoveField(
            model_name='frozenfoods',
            name='gm500_quan',
        ),
        migrations.RemoveField(
            model_name='frozenfoods',
            name='kg1',
        ),
        migrations.RemoveField(
            model_name='frozenfoods',
            name='kg1_quan',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='gm100',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='gm100_quan',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='gm250',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='gm250_quan',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='gm500',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='gm500_quan',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='kg1',
        ),
        migrations.RemoveField(
            model_name='fruits',
            name='kg1_quan',
        ),
        migrations.RemoveField(
            model_name='pulses',
            name='gm100',
        ),
        migrations.RemoveField(
            model_name='pulses',
            name='gm100_quan',
        ),
        migrations.RemoveField(
            model_name='pulses',
            name='gm250',
        ),
        migrations.RemoveField(
            model_name='pulses',
            name='gm250_quan',
        ),
        migrations.RemoveField(
            model_name='pulses',
            name='gm500',
        ),
        migrations.RemoveField(
            model_name='pulses',
            name='gm500_quan',
        ),
        migrations.RemoveField(
            model_name='pulses',
            name='kg1',
        ),
        migrations.RemoveField(
            model_name='pulses',
            name='kg1_quan',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='gm100',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='gm100_quan',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='gm250',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='gm250_quan',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='gm500',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='gm500_quan',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='kg1',
        ),
        migrations.RemoveField(
            model_name='snacks',
            name='kg1_quan',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='gm100',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='gm100_quan',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='gm250',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='gm250_quan',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='gm500',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='gm500_quan',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='kg1',
        ),
        migrations.RemoveField(
            model_name='spices',
            name='kg1_quan',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='gm100',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='gm100_quan',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='gm250',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='gm250_quan',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='gm500',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='gm500_quan',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='kg1',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='kg1_quan',
        ),
        migrations.AddField(
            model_name='bakery',
            name='cat',
            field=models.CharField(default='Bakery', max_length=20),
        ),
        migrations.AddField(
            model_name='beverages',
            name='cat',
            field=models.CharField(default='Beverages', max_length=20),
        ),
        migrations.AddField(
            model_name='beverages',
            name='desc',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='frozenfoods',
            name='cat',
            field=models.CharField(default='FrozenFoods', max_length=20),
        ),
        migrations.AddField(
            model_name='fruits',
            name='cat',
            field=models.CharField(default='Fruits', max_length=20),
        ),
        migrations.AddField(
            model_name='fruits',
            name='desc',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pulses',
            name='cat',
            field=models.CharField(default='Pulses', max_length=20),
        ),
        migrations.AddField(
            model_name='seller',
            name='landmark',
            field=models.CharField(blank=True, default=None, max_length=28, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='pin',
            field=models.CharField(blank=True, default=None, max_length=28, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=28, null=True),
        ),
        migrations.AddField(
            model_name='snacks',
            name='cat',
            field=models.CharField(default='Snacks', max_length=20),
        ),
        migrations.AddField(
            model_name='snacks',
            name='desc',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spices',
            name='cat',
            field=models.CharField(default='Spices', max_length=20),
        ),
        migrations.AddField(
            model_name='vegetables',
            name='cat',
            field=models.CharField(default='Vegetables', max_length=20),
        ),
        migrations.AddField(
            model_name='vegetables',
            name='desc',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyer',
            name='accountNumber',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='bankName',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]