# Generated by Django 3.2.12 on 2022-03-26 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street1', models.CharField(help_text='Enter street address 1', max_length=200)),
                ('street2', models.CharField(blank=True, help_text='Enter street address 2', max_length=200)),
                ('area', models.CharField(blank=True, help_text='Enter area', max_length=200)),
                ('city', models.CharField(help_text='Enter city', max_length=200)),
                ('state', models.CharField(help_text='Enter state', max_length=200)),
                ('country', models.CharField(help_text='Enter country', max_length=200)),
                ('registered_address', models.BooleanField(help_text='Click to select as registered address')),
                ('trading_address', models.BooleanField(help_text='Click to select as trading address')),
                ('directors_address', models.BooleanField(help_text='Click to select as director address')),
                ('my_bank_address', models.BooleanField(blank=True, default=False, help_text='Click to select as Bank address')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BrandToMarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_mark', models.CharField(blank=True, max_length=200)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.brands')),
            ],
        ),
        migrations.CreateModel(
            name='Markets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionToStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_to_country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.brandtomarket')),
                ('staff_permission', models.ManyToManyField(to='auth.Permission')),
                ('to_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter Company Name', max_length=200)),
                ('registration_number', models.BigIntegerField(blank=True, help_text='Enter company registration number')),
                ('auth_code', models.BigIntegerField(blank=True, help_text='Enter Authentication Code')),
                ('directors_name1', models.CharField(blank=True, help_text='Enter Directore Name', max_length=100)),
                ('directors_name2', models.CharField(blank=True, help_text='Enter Director name 2', max_length=100)),
                ('certi_incorp', models.FileField(blank=True, help_text='Upload a copy of certificate incorpation', upload_to='incorp_certificates')),
                ('business_admin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('director1_address', models.ForeignKey(blank=True, help_text='Select Director 1 Address', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_address', to='Business_Admin.address')),
                ('director2_address', models.ForeignKey(blank=True, help_text='Select Director 2 Address', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_address2', to='Business_Admin.address')),
                ('registered_address', models.ForeignKey(blank=True, help_text='Select Registration Address', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reg_address', to='Business_Admin.address')),
                ('trading_address', models.ForeignKey(blank=True, help_text='Select Trading Address', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trade_address', to='Business_Admin.address')),
            ],
        ),
        migrations.AddField(
            model_name='brandtomarket',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.markets'),
        ),
        migrations.AddField(
            model_name='brands',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.company'),
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=200)),
                ('sort_code', models.BigIntegerField(null=True)),
                ('account_number', models.BigIntegerField(null=True)),
                ('iban', models.CharField(max_length=20)),
                ('swift_code', models.CharField(max_length=20)),
                ('banks_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_address', to='Business_Admin.address')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Business_Admin.company')),
            ],
        ),
    ]
