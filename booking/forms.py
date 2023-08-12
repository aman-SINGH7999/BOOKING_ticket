from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from .models import City,Hall,Movie,Shows,User as myuser, Tcket_booking
class City_form(forms.ModelForm):
    class Meta:
        model = City
        fields = ('city_name',)
        widgets = {
            'city_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Add new city'})
        }
    # city_name = forms.CharField(label="Add new city",max_length=50)
class Movie_form(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name','movie_actor','movie_director','movie_produser','movie_about','movie_image')
        labels = {'movie_name':"Movie Name",'movie_actor':'Actor','movie_director':'Director','movie_produser':'Produser','movie_about':'Description','movie_image':'Image Link'}
        widgets = {
            'movie_name':forms.TextInput(attrs={'class':'form-control'}),
            'movie_actor':forms.TextInput(attrs={'class':'form-control'}),
            'movie_director':forms.TextInput(attrs={'class':'form-control'}),
            'movie_produser':forms.TextInput(attrs={'class':'form-control'}),
            'movie_about':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'movie_image':forms.TextInput(attrs={'class':'form-control'}),
            }

class Hall_form(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ("hall_name","city_name","hall_ratting","hall_tear")

        widgets = {
            'hall_name':forms.TextInput(attrs={'class':'form-control'}),
            'city_name':forms.TextInput(attrs={'class':'form-control'}),
            'hall_ratting':forms.NumberInput(attrs={'class':'form-control'}),
            'hall_tear':forms.NumberInput(attrs={'class':'form-control'}),
        }

class Show_form(forms.ModelForm):
    class Meta:
        model = Shows
        fields = ('date_time','gold_seat_count','platinum_seat_count','gold_seat','platinum_seat')
        labels ={
            'date_time':'Date & Time    yyyy-mm-dd hh:mm:ss',
        }
        widgets = {
            'date_time':forms.DateTimeInput(attrs={'class':'form-control'},format='%Y-%m-%d %H:%M:%S.%f'),
            'gold_seat_count':forms.NumberInput(attrs={'class':'form-control'}),
            'platinum_seat_count':forms.NumberInput(attrs={'class':'form-control'}),
            'gold_seat':forms.NumberInput(attrs={'class':'form-control'}),
            'platinum_seat':forms.NumberInput(attrs={'class':'form-control'}),
            
        }
class User_form(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }
class Booking_form(forms.ModelForm):
    class Meta:
        model = Tcket_booking
        fields = ('booking_gold_seat','booking_platinum_seat','booking_total_amount','booking_show_id','booking_user_id')

class Login_form(AuthenticationForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = User