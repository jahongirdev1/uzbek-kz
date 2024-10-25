# Generated by Django 5.0.6 on 2024-06-16 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_productmodel_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ordermodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productmodel')),
            ],
        ),
    ]
