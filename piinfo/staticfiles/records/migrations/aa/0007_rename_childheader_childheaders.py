# Generated by Django 4.2.7 on 2023-11-24 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_childheader_delete_childheaderr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChildHeader',
            new_name='ChildHeaders',
        ),
    ]