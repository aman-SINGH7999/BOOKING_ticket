# Generated by Django 4.1 on 2022-10-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_rename_password_user_user_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='booking_gold_seat',
            field=models.CharField(default='g_1', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shows',
            name='booking_platinum_seat',
            field=models.CharField(default='p_1', max_length=500),
            preserve_default=False,
        ),
    ]
