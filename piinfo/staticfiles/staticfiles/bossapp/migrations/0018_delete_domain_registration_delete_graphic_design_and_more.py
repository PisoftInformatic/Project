# Generated by Django 4.2.6 on 2023-10-18 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bossapp', '0017_delete_career_with_us_delete_hope_program_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Domain_Registration',
        ),
        migrations.DeleteModel(
            name='Graphic_Design',
        ),
        migrations.DeleteModel(
            name='Web_Design',
        ),
        migrations.DeleteModel(
            name='Web_Hosting',
        ),
        migrations.DeleteModel(
            name='Web_Marketing',
        ),
    ]