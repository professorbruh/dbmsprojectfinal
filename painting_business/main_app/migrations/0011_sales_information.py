# Generated by Django 2.0.7 on 2020-11-01 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20201101_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='sales_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.customer_information')),
                ('painting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.painting_information')),
            ],
        ),
    ]
