# Generated by Django 5.0.7 on 2024-10-28 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_information_buttons_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamousPersonalities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('desc', models.TextField(blank=True)),
                ('status', models.IntegerField(default=0)),
                ('information', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.information')),
            ],
        ),
    ]
