# Generated by Django 4.2.6 on 2023-11-01 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_services', '0011_domain_register_web_marketing_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Domain_Registration_Card',
        ),
        migrations.DeleteModel(
            name='Graphic_Design_Card',
        ),
        migrations.DeleteModel(
            name='Web_Design_Card',
        ),
        migrations.DeleteModel(
            name='Web_Marketing_Card',
        ),
        migrations.DeleteModel(
            name='Web_Services_Header',
        ),
    ]