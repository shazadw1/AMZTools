# Generated by Django 4.0.3 on 2022-04-13 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Business_Admin', '0003_alter_brandtomarket_trade_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(blank=True, max_length=100)),
                ('brand_to_market', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.brandtomarket')),
            ],
        ),
    ]