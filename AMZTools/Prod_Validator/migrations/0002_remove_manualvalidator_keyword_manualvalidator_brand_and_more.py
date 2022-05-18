# Generated by Django 4.0.3 on 2022-04-20 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Business_Admin', '0005_remove_pendingstaff_brand_to_country'),
        ('Prod_Validator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manualvalidator',
            name='keyword',
        ),
        migrations.AddField(
            model_name='manualvalidator',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.brandtomarket'),
        ),
        migrations.AddField(
            model_name='manualvalidator',
            name='keyword_auto_validate',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]