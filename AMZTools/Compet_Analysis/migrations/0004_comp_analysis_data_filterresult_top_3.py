# Generated by Django 4.0.3 on 2022-06-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compet_Analysis', '0003_alter_comp_analysis_basic_data_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp_analysis_data_filterresult',
            name='top_3',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]