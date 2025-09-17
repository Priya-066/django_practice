from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .models import Restaurant

# Create your views here.
def login(request):
    return render(request, "login.html")

def signin(request):
    return render(request, "sigin.html")

def signup(request):
    return render(request, "signup.html")

def signup1(request):
    # return HttpResponse("Received")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        password = request.POST.get("password")

        try:
            Customer.objects.get(username = username)
            return HttpResponse("Duplicates are not allowed")
        except:
            Customer.objects.create(username = username,
                                email = email,
                                mobile = mobile,
                                address = address,
                                password = password)

        return render(request, "sigin.html")
    return render(request, "signup.html")
    
def signin1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

    try:
        Customer.objects.get(username = username,password = password)
        if username == "admin":
            return render (request, "admin_home.html")
        else:
            return render(request,"customer_home.html")
        
    except Customer.DoesNotExist:
        return render(request, "fail.html")
    

def add_restaurant_page(request):
    return render(request, "add_restaurant.html")

def add_restaurant(request):
    #return HttpResponse("Working")
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        Restaurant.objects.create(name=name, 
                                  picture=picture, 
                                  cuisine=cuisine,
                                rating=rating)

        restaurants = Restaurant.objects.all()
        return render(request, 'show_restaurants.html', {"restaurants": restaurants})

    return HttpResponse("Invalid request")


    
        