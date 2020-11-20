# Generated by Django 3.0.11 on 2020-11-19 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0035_tiers_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='warehouse',
            fields=[
                ('warehouse_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Warehouse ID')),
                ('warehouse_name', models.CharField(max_length=50, verbose_name='Warehouse Name')),
                ('warehouse_paintings', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.painting_information', verbose_name='Paintings')),
            ],
        ),
        migrations.CreateModel(
            name='order_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.painting_information')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
