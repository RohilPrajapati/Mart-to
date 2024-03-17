# Generated by Django 4.1.3 on 2023-01-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_payment_payment_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='payment',
            name='total_amt',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
