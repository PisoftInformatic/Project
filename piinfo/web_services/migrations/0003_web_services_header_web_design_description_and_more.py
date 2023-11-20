# Generated by Django 4.2.6 on 2023-10-18 07:11

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_services', '0002_domain_registration_card_graphic_design_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='web_services_header',
            name='Web_Design_Description',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='web_services_header',
            name='Web_Design_Heading',
            field=models.CharField(max_length=150),
        ),
    ]