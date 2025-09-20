from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Customer
from .models import Restaurant
from .models import Item

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
            Customer.objects.get(username=username, password=password)
            if username == "admin":
                return render(request, "admin_home.html")
            else:
                restaurants = Restaurant.objects.all()
                return render(
                    request,
                    "customer_home.html",
                    {"restaurants": restaurants, "username": username}
                )
        except Customer.DoesNotExist:
            return render(request, "fail.html")

    return render(request, "sigin.html")

    

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


def open_update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'update_restaurant.html', {"restaurant": restaurant})


def open_show_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, "display_restaurants.html", {"restaurants": restaurants})

# Update Restaurant
def update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        restaurant.name = request.POST.get('name')
        restaurant.picture = request.POST.get('picture')
        restaurant.cuisine = request.POST.get('cuisine')
        restaurant.rating = request.POST.get('rating')
        restaurant.save()

        restaurants = Restaurant.objects.all()
        return render(request, 'show_restaurants.html', {"restaurants": restaurants})
    
def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == "POST":
        restaurant.delete()
        return redirect("open_show_restaurant")  # make sure this view exists!
    

def open_update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get( id=restaurant_id)
    #itemList = Item.objects.all()
    itemList = restaurant.items.all()
    return render(request, 'update_menu.html', {"itemList": itemList, "restaurant": restaurant})


def update_menu(request,restaurant_id ):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        is_veg = request.POST.get('is_veg') == 'on'
        picture = request.POST.get('picture')

        
        Item.objects.create(
            restaurant=restaurant,
            name=name,
            description=description,
            price=price,
            is_veg=is_veg,
            picture=picture
        )
        return render(request, 'admin_home.html')
    

def view_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    itemList = restaurant.items.all()
    return render(
        request,
        'customer_menu.html',
        {"itemList": itemList, "restaurant": restaurant}
    )
        