# Generated by Django 2.0.7 on 2020-11-02 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20201102_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_information',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.customer_information'),
        ),
    ]
