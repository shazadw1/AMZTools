# Generated by Django 3.2.12 on 2022-02-24 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Business_Admin', '0004_auto_20220224_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressmodel',
            name='company',
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companymodel',
            name='bank_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_address', to='Business_Admin.addressmodel'),
        ),
        migrations.AddField(
            model_name='companymodel',
            name='directors_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_address', to='Business_Admin.addressmodel'),
        ),
        migrations.AddField(
            model_name='companymodel',
            name='registered_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reg_address', to='Business_Admin.addressmodel'),
        ),
        migrations.AddField(
            model_name='companymodel',
            name='trading_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trade_address', to='Business_Admin.addressmodel'),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='area',
            field=models.CharField(blank=True, help_text='Enter area', max_length=200),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='city',
            field=models.CharField(help_text='Enter city', max_length=200),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='country',
            field=models.CharField(help_text='Enter country', max_length=200),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='directors_address',
            field=models.BooleanField(help_text='Enter director address'),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='registered_address',
            field=models.BooleanField(help_text='Enter registered address'),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='state',
            field=models.CharField(help_text='Enter state', max_length=200),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='street1',
            field=models.CharField(help_text='Enter street address 1', max_length=200),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='street2',
            field=models.CharField(blank=True, help_text='Enter street address 2', max_length=200),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='trading_address',
            field=models.BooleanField(help_text='Enter trading address'),
        ),
    ]