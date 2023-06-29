from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User,Product,Orders
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import JsonResponse
from json import loads
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def index(request):
    products = Product.objects.all().order_by('-id')
    paginator = Paginator(products, 10)
    page = request.GET.get('page',1)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    return render(request, "store/index.html",{'products': product})

def Search(request):
    q = request.GET["q"]
    result = Product.objects.filter(NameProduct__contains=q)
    return render(request, "store/page.html",{'search': result})

def About(request):
    return render(request, "store/page.html")


def register_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmpassword"]
        if password != confirmation:
            return render(request, "store/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username= email,first_name=name,email=email,password=password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Email already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "store/register.html")

def login_view(request):
    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "store/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "store/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def NewProduct(request):
    if request.user.id:
        if request.method == "POST":
                name = request.POST.get('ProductName').capitalize()
                description  = request.POST.get('ProductDescription')
                image  = request.POST.get('ProductImage')
                price  = request.POST.get('Price')
                quantity  = request.POST.get('Quantity')
                newProduct = Product(NameProduct=name,Description=description,Img=image,Price=price,Quantity=quantity)
                newProduct.save()
                return HttpResponseRedirect(reverse("admin:index"))
        return render(request, "store/index.html")
    else:
         return render(request, "store/login.html")

@login_required
def product_view(request,product_id):
    Productt = Product.objects.get(id=product_id)
    return render(request, "store/product.html", {
     "Product": Productt
    })

@csrf_exempt
@login_required
def NewOrder(request):
    if request.method == "POST":
        data = loads(request.body)
        productid = data["productid"]
        productprice = data["productprice"]
        productqty = data["productqty"]
        Remains = data["Remains"]
        product = Product.objects.get(id=productid)
        newOrdert = Orders(UserID=request.user,ProdictID=product,Number=productqty,TotalPrice=productprice)
        newOrdert.save()
        product.Quantity = Remains
        product.save(update_fields=["Quantity"])

        return JsonResponse({
            "message": "Your order has been successfully placed"
        }, status=200)
        # return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "Error! There was a problem placing the order"
        }, status=400)

def Orders_views(request):
    Ordersall = Orders.objects.filter(UserID=request.user)
    return render(request, "store/orders.html",{'Orders': Ordersall})

def profile_views(request):
    profileUser = User.objects.get(id=request.user.id)
    return render(request, "store/page.html", {
     "puser": profileUser
    }) 

@login_required
def profile_save(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        user.username  = request.POST.get('Email')
        user.first_name = request.POST.get('FirstName')
        user.last_name  = request.POST.get('LastName')
        user.email  = request.POST.get('Email')
        user.Address  = request.POST.get('Address')
        user.ZipCode  = request.POST.get('ZipCode')
        user.save(update_fields=["username", "first_name", "last_name", "email", "Address", "ZipCode"])
        return HttpResponseRedirect(reverse("profile"))
    return render(request, "network/index.html")
