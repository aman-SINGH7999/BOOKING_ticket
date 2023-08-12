from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User as USER

# Create your models here.
class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)
    seat_type = models.CharField(max_length=30)
    seat_status = models.BooleanField()
    seat_price = models.IntegerField()

class Hall(models.Model):
    hall_id = models.AutoField(primary_key=True)
    hall_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=50)
    hall_ratting = models.FloatField()
    hall_tear = models.IntegerField()
    gold_price = models.IntegerField()
    platinum_price = models.IntegerField()
    # hall_screan = models.IntegerField()

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=50)
    movie_actor = models.CharField(max_length=50)
    movie_director = models.CharField(max_length=50)
    movie_produser = models.CharField(max_length=50)
    movie_about = models.CharField(max_length=500)
    movie_image = models.CharField(max_length=100)

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_mail = models.EmailField()
    user_pass = models.CharField(max_length=300)

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    movie_id = models.IntegerField()
    seat_id = models.IntegerField()
    user_id = models.IntegerField()

class Shows(models.Model):
    show_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    gold_seat = models.IntegerField()
    platinum_seat = models.IntegerField()
    gold_seat_count = models.IntegerField()
    platinum_seat_count = models.IntegerField()
    booking_gold_seat = models.CharField(max_length=500,blank=True)
    booking_platinum_seat = models.CharField(max_length=500,blank=True)
    hall = models.ForeignKey('Hall',on_delete = models.CASCADE)
    movie = models.ForeignKey('Movie',on_delete = models.CASCADE)
    
class Tcket_booking(models.Model):
    Tcket_booking_id = models.AutoField(primary_key=True)
    booking_gold_seat = models.CharField(max_length=300,blank=True)
    booking_platinum_seat = models.CharField(max_length=300,blank=True)
    booking_total_amount = models.IntegerField()
    booking_show_id = models.IntegerField()
    booking_user_id = models.IntegerField()