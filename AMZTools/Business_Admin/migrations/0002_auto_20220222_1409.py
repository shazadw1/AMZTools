# Generated by Django 3.2.12 on 2022-02-22 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Business_Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('registration_number', models.BigIntegerField(blank=True, max_length=20)),
                ('auth_code', models.BigIntegerField(blank=True, max_length=20)),
                ('directors_name1', models.CharField(blank=True, max_length=100)),
                ('directors_name2', models.CharField(blank=True, max_length=100)),
                ('certi_incorp', models.FileField(blank=True, upload_to='incorp_certificates')),
                ('business_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.companymodel'),
        ),
    ]
