# Generated by Django 5.0.7 on 2024-08-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_branchmodel_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchmodel',
            name='orderList',
            field=models.ManyToManyField(blank=True, related_name='order_list', to='main.ordermodel'),
        ),
    ]
