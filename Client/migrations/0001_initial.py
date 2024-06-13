# Generated by Django 5.0.6 on 2024-06-13 07:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_method',
            fields=[
                ('payment_method_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'payment_method',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('tax_id', models.AutoField(primary_key=True, serialize=False)),
                ('tax_name', models.CharField(max_length=155)),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'tax',
            },
        ),
        migrations.CreateModel(
            name='Technology_option',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False)),
                ('option', models.CharField(max_length=155)),
            ],
            options={
                'db_table': 'technology_option',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=255)),
                ('company_address', models.CharField(max_length=555)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_client', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('tech_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('option_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.technology_option')),
            ],
            options={
                'db_table': 'technology',
            },
        ),
    ]
