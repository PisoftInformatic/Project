# Generated by Django 4.2.6 on 2023-11-01 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career_and_intern', '0002_alter_career_with_us_job_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='career_with_us',
            options={'verbose_name_plural': 'Career With Us'},
        ),
        migrations.AlterModelOptions(
            name='hope_program',
            options={'verbose_name_plural': 'Hop Program'},
        ),
        migrations.AlterModelOptions(
            name='six_weeks_intern',
            options={'verbose_name_plural': 'Six weeks internship'},
        ),
        migrations.AlterModelOptions(
            name='tech_descovery',
            options={'verbose_name_plural': 'Tech Discovery'},
        ),
        migrations.AlterModelOptions(
            name='traniee_with_us',
            options={'verbose_name_plural': 'Trainee With us'},
        ),
    ]