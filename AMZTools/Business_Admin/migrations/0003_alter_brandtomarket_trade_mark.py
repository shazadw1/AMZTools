# Generated by Django 4.0.3 on 2022-04-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business_Admin', '0002_alter_company_business_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandtomarket',
            name='trade_mark',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
