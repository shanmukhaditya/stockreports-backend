# Generated by Django 4.2 on 2023-05-05 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockreports', '0002_rename_stocks_stockreports'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StockReports',
            new_name='Stocks',
        ),
    ]
