# Generated by Django 4.1 on 2022-10-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_shows_gold_seat_shows_gold_seat_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='city_id',
        ),
        migrations.AddField(
            model_name='hall',
            name='city_name',
            field=models.CharField(default='varansi', max_length=50),
            preserve_default=False,
        ),
    ]