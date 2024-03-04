# Generated by Django 4.2.7 on 2023-11-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_alter_apply_job_options_alter_contact_data_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=50)),
                ('module_price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Modules',
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobileno', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
    ]