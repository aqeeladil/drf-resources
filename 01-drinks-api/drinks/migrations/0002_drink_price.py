# Generated by Django 5.1.7 on 2025-03-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
