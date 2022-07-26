# Generated by Django 4.0.3 on 2022-06-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compet_Analysis', '0005_remove_comp_analysis_kw_cerebro_data_asin11_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp_analysis_kw_cerebro_data_head',
            name='excel_file',
            field=models.FileField(blank=True, upload_to='compt_analysis/final_cerebro_excel'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_basic_data',
            name='amazon_choice',
            field=models.FileField(blank=True, upload_to='compt_analysis/amazon choice'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_basic_data',
            name='cerebro',
            field=models.FileField(blank=True, upload_to='compt_analysis/cerebro'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_basic_data',
            name='google_trends_ss',
            field=models.FileField(blank=True, upload_to='compt_analysis/google trends ss'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_basic_data',
            name='magnet',
            field=models.FileField(blank=True, upload_to='compt_analysis/magnet'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_basic_data',
            name='xray',
            field=models.FileField(blank=True, upload_to='compt_analysis/xray'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_basic_data',
            name='xray_graph',
            field=models.FileField(blank=True, upload_to='compt_analysis/x-ray graphs'),
        ),
        migrations.AlterField(
            model_name='comp_analysis_basic_data',
            name='xray_ss',
            field=models.FileField(blank=True, upload_to='compt_analysis/x-ray ss'),
        ),
    ]