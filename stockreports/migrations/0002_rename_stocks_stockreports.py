# Generated by Django 4.2 on 2023-05-03 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockreports', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stocks',
            new_name='StockReports',
        ),
    ]
