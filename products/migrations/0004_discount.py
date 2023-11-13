# Generated by Django 4.2.7 on 2023-11-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_shoppingcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('multiple_usage', models.BooleanField()),
                ('percent', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
