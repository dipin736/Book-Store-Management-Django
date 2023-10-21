# Generated by Django 4.1.5 on 2023-10-19 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Credict Card', 'Credict Card'), ('G-Pay', 'G-pay'), ('Paypal', 'Paypal')], default='Paypal', max_length=20),
        ),
        migrations.CreateModel(
            name='orderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.order')),
            ],
        ),
    ]
