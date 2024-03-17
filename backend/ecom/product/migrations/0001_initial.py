# Generated by Django 4.1.3 on 2022-11-19 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product')),
                ('price', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('entry_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
