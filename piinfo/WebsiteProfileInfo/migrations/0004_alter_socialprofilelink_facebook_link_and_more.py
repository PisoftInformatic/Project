# Generated by Django 5.0.1 on 2024-01-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteProfileInfo', '0003_alter_websiteprofiledata_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialprofilelink',
            name='facebook_link',
            field=models.CharField(blank=True, default='https://www.pisoftinformatics.com', help_text='Enter Facebook link that starts with https. ex: https://www.facebook.com/xyz ', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='socialprofilelink',
            name='linkedin_link',
            field=models.CharField(blank=True, default='https://www.pisoftinformatics.com', help_text='Enter Linkedin link that starts with https. ex: https://www.linkedin.com/xyz ', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='socialprofilelink',
            name='twitter_link',
            field=models.CharField(blank=True, default='https://www.pisoftinformatics.com', help_text='Enter Twitter link that starts with https. ex: https://www.twitter.com/xyz ', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='socialprofilelink',
            name='youtube_link',
            field=models.CharField(blank=True, default='https://www.pisoftinformatics.com', help_text='Enter Youtube link that starts with https. ex: https://www.youtube.com/xyz ', max_length=150, null=True),
        ),
    ]