# Generated by Django 3.2.12 on 2022-03-09 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business_Admin', '0004_auto_20220309_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='directors_address',
            field=models.BooleanField(help_text='Click to select as director address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='my_bank_address',
            field=models.BooleanField(blank=True, default=False, help_text='Click to select as Bank address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='registered_address',
            field=models.BooleanField(help_text='Click to select as registered address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='trading_address',
            field=models.BooleanField(help_text='Click to select as trading address'),
        ),
    ]
