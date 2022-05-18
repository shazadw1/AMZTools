# Generated by Django 4.0.3 on 2022-04-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prod_Validator', '0004_manualvalidatorhead_asin11_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin10',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin11',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin2',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin3',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin4',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin5',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin6',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin7',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin8',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='asin9',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='phrase',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='position',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='search_volume',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='manualvalidatordata',
            name='title_density',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='manualvalidator',
            name='amazon_choice',
            field=models.FileField(upload_to='manual_validator/amazon choice'),
        ),
        migrations.AlterField(
            model_name='manualvalidator',
            name='cerebro',
            field=models.FileField(upload_to='manual_validator/cerebro'),
        ),
        migrations.AlterField(
            model_name='manualvalidator',
            name='google_trends_ss',
            field=models.FileField(upload_to='manual_validator/google trends ss'),
        ),
        migrations.AlterField(
            model_name='manualvalidator',
            name='magnet',
            field=models.FileField(upload_to='manual_validator/magnet'),
        ),
        migrations.AlterField(
            model_name='manualvalidator',
            name='xray',
            field=models.FileField(upload_to='manual_validator/xray'),
        ),
        migrations.AlterField(
            model_name='manualvalidator',
            name='xray_graph',
            field=models.FileField(upload_to='manual_validator/x-ray graphs'),
        ),
        migrations.AlterField(
            model_name='manualvalidator',
            name='xray_ss',
            field=models.FileField(upload_to='manual_validator/x-ray ss'),
        ),
    ]