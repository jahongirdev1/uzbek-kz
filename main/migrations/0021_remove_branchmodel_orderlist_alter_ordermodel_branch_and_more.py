# Generated by Django 5.0.7 on 2024-08-16 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_ordermodel_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branchmodel',
            name='orderList',
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='main.branchmodel'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='productsList',
            field=models.ManyToManyField(related_name='order_products', to='main.productmodel'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to='main.usermodel'),
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='orders',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to='main.ordermodel'),
        ),
    ]