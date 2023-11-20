# Generated by Django 4.2.6 on 2023-11-01 08:48

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_services', '0010_web_design_alter_graphic_design_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_heading', models.CharField(help_text='Main Heading of the Page', max_length=50)),
                ('page_description', models.TextField(help_text='Description of the page. ')),
            ],
            options={
                'verbose_name_plural': 'Domain Register',
            },
        ),
        migrations.CreateModel(
            name='Web_Marketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_heading', models.CharField(help_text='Main Heading of the Page', max_length=50)),
                ('page_description', models.TextField(help_text='Description of the page. ')),
            ],
            options={
                'verbose_name_plural': 'Web Marketing',
            },
        ),
        migrations.AlterField(
            model_name='web_design_box',
            name='package_description',
            field=tinymce.models.HTMLField(blank=True, max_length=350),
        ),
        migrations.CreateModel(
            name='Web_Marketing_Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(blank=True, help_text='Enter your Package name eg. Platinum, Gold or Basic,Advanced', max_length=50)),
                ('service', models.CharField(blank=True, help_text='Services tha you offers.. eg.- static, dynamic site, wordress etc.', max_length=50)),
                ('package_description', tinymce.models.HTMLField(blank=True, max_length=350)),
                ('card', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web_services.web_marketing')),
            ],
            options={
                'verbose_name_plural': 'Web Marketing Features and Prices',
            },
        ),
        migrations.CreateModel(
            name='Domain_Register_Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(blank=True, help_text='Enter your Package name eg. Platinum, Gold or Basic,Advanced', max_length=50)),
                ('service', models.CharField(blank=True, help_text='Services tha you offers.. eg.- static, dynamic site, wordress etc.', max_length=50)),
                ('package_description', tinymce.models.HTMLField(blank=True, max_length=350)),
                ('card', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web_services.domain_register')),
            ],
            options={
                'verbose_name_plural': 'Domain Register Features and Prices',
            },
        ),
    ]