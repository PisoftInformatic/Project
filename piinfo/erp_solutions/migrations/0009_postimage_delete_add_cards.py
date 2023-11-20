# Generated by Django 4.2.6 on 2023-10-31 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_solutions', '0008_add_cards_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='erp_solutions.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Add_Cards',
        ),
    ]