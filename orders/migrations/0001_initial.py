# Generated by Django 4.2.7 on 2023-12-04 11:44

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=256)),
                ('address1', models.CharField(max_length=256)),
                ('address2', models.CharField(blank=True, max_length=256, null=True)),
                ('country', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=64)),
                ('orders_history', models.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Processing'), (2, 'Cancelled'), (3, 'Out for delivery'), (4, 'Delivered'), (5, 'Refunded')], default=1)),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
