# Generated by Django 4.1 on 2022-10-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_movie_movie_image_alter_movie_movie_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='gold_seat',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shows',
            name='gold_seat_count',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shows',
            name='platinum_seat',
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shows',
            name='platinum_seat_count',
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
    ]