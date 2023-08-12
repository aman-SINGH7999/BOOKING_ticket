from django.shortcuts import render
from django.contrib import messages
from .models import City, Movie, Hall, Shows
from .forms import City_form, Movie_form, Hall_form, Show_form,User_form, Booking_form, Login_form
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login as l_in, logout as l_out
# from django.contrib.auth.models import User
# Create your views here.
# --------------------------------------------------------------------------------------home
def home(request):
    movie = Movie.objects.all().order_by('-movie_id').values()
    # movie.reverse()
    movie_list = []
    n = 3;
    if n > len(movie):
        n = len(movie)
    for i in range(n):
        movie_list.append(movie[i])

    # movie_list = movie_list[-1::-1]
    return render(request,'booking/home.html',{'movies':movie,'carousel':movie_list})

# ------------------------------------------------------------------------------------------about
def about(request,id):
    movies = Movie.objects.get(pk=id)
    shows = Shows.objects.filter(movie_id = movies.movie_id).select_related()
    if request.method == 'POST':
        return render(request,'booking/booking.html',{})
    # print(shows)
    return render(request,'booking/about.html',{'movies':movies,'shows':shows})

# -------------------------------------------------------------------------------------------login
def login(request):
    if not request.user.is_authenticated:
        form = Login_form()
        if request.method == 'POST':
            form = Login_form(request=request, data = request.POST)
            print(form)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                print(uname,upass)
                if user is not None:
                    l_in(request,user)
                past = request.POST.get('past')
                return HttpResponseRedirect(past if past else "/") #past if past else "/"
        return render(request,'booking/login.html',{'forms':form})
    else:
        return HttpResponseRedirect('/')
    


def signup(request):
    form = User_form()
    if request.method == 'POST':
        form = User_form(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.info(request,"Please signupn if you are not!")
            return HttpResponseRedirect('/signup/')
    return render(request,'booking/signup.html',{'forms':form})
# -------------------------------------------------------------------------------------------logout
def user_logout(request):
    l_out(request)
    return HttpResponseRedirect("/")
# ------------------------------------------------------------------------------------------booking
def booking(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/?past='+request.GET.get('past'))
    else:
        # return HttpResponseRedirect('/login/')
        pi = Shows.objects.get(pk=id)
        show_id = pi.show_id
        goldseats = pi.gold_seat_count
        platinumseats = pi.platinum_seat_count

        bookinggold = pi.booking_gold_seat
        bookinggoldseat = bookinggold.split(',')
        # print(bookinggoldseat)
        gold_seat_list = []
        for i in bookinggoldseat:
            try:
                n = int(i.split('_')[1])
                gold_seat_list.append(n)
            except:
                pass

        bookingplatinum = pi.booking_platinum_seat
        bookingplatinumseat = bookingplatinum.split(',')
        platinum_seat_list = []
        for i in bookingplatinumseat:
            try:
                n = int(i.split('_')[1])
                platinum_seat_list.append(n)
            except:
                pass

        gold_price = pi.hall.gold_price
        platinum_price = pi.hall.platinum_price
        print(gold_price,platinum_price)
        form = Booking_form()
        if request.method == 'POST':

            form = Booking_form(request.POST)
            form.booking_show_id = show_id
            print(request.POST)
            if form.is_valid():
                g_seat = form.cleaned_data['booking_gold_seat']
                p_seat = form.cleaned_data['booking_platinum_seat']

                print(pi.booking_gold_seat,g_seat)
                print(pi.booking_platinum_seat,p_seat)
                GOLD_seat = pi.booking_gold_seat+','+g_seat;
                PLATINUM_seat = pi.booking_platinum_seat+','+p_seat;
                list_gold = set(GOLD_seat.split(','))
                list_platinum = set(PLATINUM_seat.split(','))
                list_gold = list(list_gold)
                if "" in list_gold:
                    list_gold.remove("")
                list_platinum = list(list_platinum)
                if "" in list_platinum:
                    list_platinum.remove("")
                # print(",".join(list_gold))
                # print(list_gold,len(list_gold))
                # print(list_platinum,len(list_platinum))

                pi.gold_seat = pi.gold_seat_count - len(list_gold)
                pi.platinum_seat = pi.platinum_seat_count - len(list_platinum)
                pi.booking_gold_seat = ",".join(list_gold);
                pi.booking_platinum_seat = ",".join(list_platinum);
                if len(g_seat) > 1:
                    g_seat_pay = len(g_seat.split(','))*gold_price
                else:
                    g_seat_pay = 0
                if len(p_seat) > 1:
                    p_seat_pay = len(p_seat.split(','))*platinum_price
                else:
                    p_seat_pay = 0
                print("-----------------------------------------",g_seat_pay,p_seat_pay)
                
                pi.save()
                
                pay = g_seat_pay+p_seat_pay
                return render(request,'booking/ticket.html',{'pay':pay,"pi":pi})
                # print(g_seat,p_seat)
                # return HttpResponseRedirect('/booking/')

        return render(request,'booking/booking.html',{'show_id':show_id,'forms':form,'goldseats':goldseats,'pltmseats':platinumseats,'gold_seat_list':gold_seat_list,'platinum_seat_list':platinum_seat_list,'gold_price':gold_price,'platinum_price':platinum_price})
# ==============================================

def ticket(request):
    return render(request,'booking/ticket.html')

# --------------------------------------------------------------------------------------------admin
def admin(request):
    return render(request,'booking/admin.html')
# --------------------------------------------------------------------------------------------------cities
def cities(request):
    if request.method == "POST":
        form = City_form(request.POST)
        if form.is_valid():
            messages.success(request,'City Added!')
            form.save()
            city = City.objects.all()
            return HttpResponseRedirect('/cities/')
    else:
        form = City_form() 
        city = City.objects.all()
        return render(request,'booking/cities.html',{'cities':city,'forms':form})

def deletecity(request,id):
    if request.method == 'POST':
        city = City.objects.get(pk=id)
        city.delete()
        return HttpResponseRedirect('/cities/')

def updatecity(request,id):
    if request.method == 'POST':
        pi = City.objects.get(pk=id)
        fm = City_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/cities/')
        else:
            fm = City_form(instance=pi)
            return render(request,'booking/updatecity.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/cities/')

# -----------------------------------------------------------------------------------------------------movies
def movies(request):
    movie = Movie.objects.all()
    form = Movie_form()
    if request.method == 'POST':
        form = Movie_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movies/')
        else:
            return render(request,'booking/movies.html',{'movies':movie,'addforms':form})  
    return render(request,'booking/movies.html',{'movies':movie,'addforms':form})

def deletemovie(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return HttpResponseRedirect('/movies/')

def updatemovie(request,id):
    # print('-------------------------------------id ================================= ',id)
    if request.method == 'POST':
        pi = Movie.objects.get(pk=id)
        fm = Movie_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/movies/') 
    return HttpResponseRedirect('/movies/')

# --------------------------------------------------------------------------------------------------------shows
def shows(request):
    show = Shows.objects.all()
    halls = Hall.objects.values_list("hall_id", "hall_name")
    movies = Movie.objects.values_list("movie_id", "movie_name")
    if request.method == 'POST':
        form = Show_form(request.POST)
        if form.is_valid():
            date_time = form.cleaned_data['date_time']
            gold_seat = form.cleaned_data['gold_seat']
            platinum_seat = form.cleaned_data['platinum_seat']
            gold_seat_count = form.cleaned_data['gold_seat_count']
            platinum_seat_count = form.cleaned_data['platinum_seat_count']
            movie_ids = request.POST.get("movie")
            movie = Movie.objects.get(movie_id = movie_ids)
            hall_ids = request.POST.get("hall")
            hall = Hall.objects.get(hall_id = hall_ids)
            # print(movie,hall)
            Shows.objects.create(
                date_time = date_time,
                gold_seat = gold_seat,
                platinum_seat = platinum_seat,
                gold_seat_count = gold_seat_count,
                platinum_seat_count = platinum_seat_count,
                hall = hall,
                movie = movie
            )
            return HttpResponseRedirect('/shows/')
    form = Show_form()
    return render(request,'booking/shows.html',{'shows':show,'addforms':form, 'halls': halls, 'movies': movies})

def updateshow(request,id):
    # print('---------------------------------------------------------')
    pi = Shows.objects.get(pk=id)
    form = Show_form(instance=pi)
    if request.method == 'POST':
        form = Show_form(request.POST,instance=pi)
        # print(form)
        if form.is_valid():
            # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            date_time = form.cleaned_data['date_time']
            gold_seat = form.cleaned_data['gold_seat']
            platinum_seat = form.cleaned_data['platinum_seat']
            gold_seat_count = form.cleaned_data['gold_seat_count']
            platinum_seat_count = form.cleaned_data['platinum_seat_count']
            movie_ids = request.POST.get("movie")
            movie = Movie.objects.get(movie_id = movie_ids)
            hall_ids = request.POST.get("hall")
            hall = Hall.objects.get(hall_id = hall_ids)
            # print(movie,hall, )
            pi.date_time = date_time
            pi.gold_seat = gold_seat
            pi.platinum_seat = platinum_seat
            pi.gold_seat_count = gold_seat_count
            pi.platinum_seat_count = platinum_seat_count
            pi.hall = hall
            pi.movie = movie
            pi.save()
            return HttpResponseRedirect('/shows/')
    return HttpResponseRedirect('/shows/')

def deleteshow(request,id):
    if request.method == 'POST':
        show = Shows.objects.get(pk=id)
        show.delete()
        return HttpResponseRedirect('/shows/')

# -----------------------------------------------------------------------------------------------------halls
def halls(request):
    hall = Hall.objects.all()
    if request.method == 'POST':
        fm = Hall_form(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/halls/')
    else:
        fm = Hall_form()
    return render(request,'booking/halls.html',{'halls':hall,'addforms':fm})

def deletehall(request,id):
    if request.method == 'POST':
        hall = Hall.objects.get(pk=id)
        hall.delete()
        return HttpResponseRedirect('/halls/')

def updatehall(request,id):
    print("******************************8")
    if request.method == 'POST':
        pi = Hall.objects.get(pk=id)
        fm = Hall_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/halls/')
    return HttpResponseRedirect('/halls/')
       
    
# ----------------------------------------------------------------------------------------------------booking
def tcket_booking(request):
    pass
