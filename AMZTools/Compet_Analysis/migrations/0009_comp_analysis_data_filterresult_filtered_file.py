# Generated by Django 4.0.3 on 2022-07-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compet_Analysis', '0008_comp_analysis_kw_master_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp_analysis_data_filterresult',
            name='filtered_file',
            field=models.FileField(blank=True, upload_to='compt_analysis/fi;tered_cerebro_excel/'),
        ),
    ]