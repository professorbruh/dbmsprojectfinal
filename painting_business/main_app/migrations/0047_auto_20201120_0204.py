# Generated by Django 3.0.11 on 2020-11-19 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0046_warehouse_painting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse_painting',
            name='paint',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.painting_information', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='warehouse_painting',
            name='ware',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.warehouse', verbose_name='Warehouse ID'),
        ),
    ]
