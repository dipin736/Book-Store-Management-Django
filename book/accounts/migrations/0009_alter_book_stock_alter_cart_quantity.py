# Generated by Django 4.1.5 on 2023-10-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_book_price_alter_book_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
