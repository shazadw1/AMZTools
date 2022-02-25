# Generated by Django 3.2.12 on 2022-02-24 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Business_Admin', '0008_remove_markets_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='markets',
            name='trade_mark',
        ),
        migrations.AddField(
            model_name='brands',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.markets'),
        ),
        migrations.AddField(
            model_name='brands',
            name='trade_mark',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]