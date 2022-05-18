# Generated by Django 3.2.12 on 2022-03-26 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_app', models.CharField(blank=True, max_length=100)),
                ('display_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Name', max_length=100)),
                ('pricing_per_month', models.IntegerField(help_text='Enter Price for per month')),
                ('description', models.CharField(help_text='Enter Description', max_length=100)),
                ('company_limit', models.IntegerField(help_text='Enter Company Limit')),
                ('users_limit', models.IntegerField(help_text='Enter Users Limit')),
                ('brands_limit', models.IntegerField(help_text='Enter Brand Limit')),
                ('markets_limit', models.IntegerField(help_text='Enter Markets Limit')),
                ('product_validation_limit', models.IntegerField(help_text='Enter Product Validation Limit')),
                ('comp_analysis_limit', models.IntegerField(help_text='Enter Company Analysis limit')),
                ('listings_limit', models.IntegerField(help_text='Enter Listing Limit')),
                ('ppc_generation_limit', models.IntegerField(help_text='Enter PPC Generation Limit')),
                ('ppc_optimization_limit', models.IntegerField(help_text='Enter PPC Optimization Limit')),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModulePlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_list', models.ManyToManyField(to='Plans.AppList')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Plans.package')),
            ],
        ),
        migrations.CreateModel(
            name='Business_Admin_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Plans.package')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
