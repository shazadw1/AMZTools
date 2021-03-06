# Generated by Django 4.0.3 on 2022-06-19 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Business_Admin', '0005_remove_pendingstaff_brand_to_country'),
        ('Compet_Analysis', '0002_comp_analysis_data_filter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comp_analysis_basic_data',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.brandtomarket'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_kw_amz_choice_data',
            name='brand_to_market',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Compet_Analysis.comp_analysis_basic_data'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_kw_ba_data',
            name='brand_to_market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.brandtomarket'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_kw_ba_output_data',
            name='brand_to_market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.brandtomarket'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_kw_magnet_data',
            name='brand_to_market',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Compet_Analysis.comp_analysis_basic_data'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_kw_master_kw_data',
            name='brand_to_market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.brandtomarket'),
        ),
    ]
