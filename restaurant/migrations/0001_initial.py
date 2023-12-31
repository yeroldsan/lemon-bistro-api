# Generated by Django 4.2.3 on 2023-07-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('guests_number', models.SmallIntegerField(default=1)),
                ('reservation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=6)),
                ('inventory', models.IntegerField()),
                ('menu_item_description', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
