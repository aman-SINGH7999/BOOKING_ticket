# Generated by Django 4.1 on 2022-10-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_alter_tcket_booking_booking_gold_seat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='booking_gold_seat',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='shows',
            name='booking_platinum_seat',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
