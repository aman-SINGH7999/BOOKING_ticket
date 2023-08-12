from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/<int:id>/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('ticket/',views.ticket,name='ticket'),
    path('booking/<int:id>',views.booking,name='booking'),
    path('user-logout/',views.user_logout,name='user-logout'),
    path('myadmin/',views.admin,name='admin'),

    path('cities/',views.cities,name='cities'),
    path('cities/<int:id>/',views.deletecity,name='deletecity'),
    path('updatecity/<int:id>/',views.updatecity,name='updatecity'),

    path('movies/',views.movies,name='movies'),
    path('movies/<int:id>/',views.deletemovie,name='deletemovie'),
    path('updatemovie/<int:id>/',views.updatemovie,name='updatemovie'),

    path('shows/',views.shows,name='shows'),
    path('shows/<int:id>',views.deleteshow,name='deleteshow'),
    path('updateshow/<int:id>',views.updateshow,name='updateshow'),

    # path('bookings/',views.bookings,name='bookings'),

    path('halls/',views.halls,name='halls'),
    path('halls/<int:id>',views.deletehall,name='deletehall'),
    path('updatehall/<int:id>',views.updatehall,name='updatehall'),
    
    path('Tcket_booking/',views.tcket_booking,name='Tcket_booking')

]
