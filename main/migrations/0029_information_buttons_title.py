# Generated by Django 5.0.7 on 2024-10-27 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_news_status_region_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='buttons_title',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
