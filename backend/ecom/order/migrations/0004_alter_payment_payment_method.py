# Generated by Django 4.1.3 on 2023-01-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_payment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'cash'), ('online', 'online')], max_length=10),
        ),
    ]
