from atexit import register
from django.contrib import admin
from .import models
# Register your models here.
@admin.register(models.Seat)
class SeatModel(admin.ModelAdmin):
    list_display = ('seat_id','seat_type','seat_status','seat_price')

@admin.register(models.Hall)
class HallModel(admin.ModelAdmin):
    list_display = ('hall_id','hall_name','city_name','hall_ratting','hall_tear')

@admin.register(models.Movie)
class MovieModel(admin.ModelAdmin):
    list_display = ('movie_id','movie_name','movie_actor','movie_director','movie_produser','movie_image')

@admin.register(models.City)
class CityModel(admin.ModelAdmin):
    list_display = ('city_id','city_name')

@admin.register(models.User)
class UserModel(admin.ModelAdmin):
    list_display = ('user_id','user_name','user_mail','user_pass')

@admin.register(models.Ticket)
class TicketModel(admin.ModelAdmin):
    list_display = ('ticket_id','movie_id','seat_id','user_id')

@admin.register(models.Shows)
class ShowsModel(admin.ModelAdmin):
    list_display = ('show_id','movie','hall','date_time','gold_seat_count','gold_seat','platinum_seat_count','platinum_seat','booking_gold_seat','booking_platinum_seat')

@admin.register(models.Tcket_booking)
class Tcket_booking_Model(admin.ModelAdmin):
    list_display = ('Tcket_booking_id','booking_gold_seat','booking_platinum_seat','booking_total_amount','booking_show_id','booking_user_id')
