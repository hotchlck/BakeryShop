import datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import item
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/login')
def show_main(request):
    items = item.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'items' : items,
        'last_login': request.COOKIES['last_login'],
        'total_items': items.__len__(),
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_item(request, id_item):
    product = get_object_or_404(item, pk=id_item, user=request.user)
    product.amount += 1
    product.save()
    return redirect('main:show_main')

def minus_item(request, id_item):
    product = get_object_or_404(item, pk=id_item, user=request.user)
    if product.amount >0:
        product.amount -= 1
        product.save()
    else: 
        messages.info(request, f'Tidak dapat mengurangi jumlah produk! Total {product.name} berjumlah 0 ')
    return redirect('main:show_main')

def remove_item(request, id_item):
    product = get_object_or_404(item, pk=id_item, user=request.user)
    product.delete()
    return redirect('main:show_main')

def get_product_json(request):
    product = item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        image_url = request.POST.get("image_url")
        user = request.user

        new_product = item(name=name, price=price, amount=amount ,description=description, image_url=image_url ,user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='login/')
@csrf_exempt
def increment_ajax(request):
    if request.method == 'POST':
        pk = json.loads(request.body).get('pk')
        product = item.objects.get(pk=pk, user=request.user)
        product.amount += 1
        product.save()
        return HttpResponse(b"OK", status=200)
    
    return HttpResponseNotFound()

@login_required(login_url='login/')
@csrf_exempt 
def decrement_ajax(request):
    if request.method == 'POST':
        pk = json.loads(request.body).get('pk')
        product = item.objects.get(pk=pk, user=request.user)
        if (product.amount > 0):
            product.amount -= 1
            product.save()
        else: # jika stok produk sudah habis = delete
            product.delete()
        return HttpResponse(b"OK", status=200)
    
    return HttpResponseNotFound()

@login_required(login_url='login/')
@csrf_exempt
def delete_ajax(request):
    if request.method == 'POST':
        pk = json.loads(request.body).get('pk')
        product = item.objects.get(pk=pk, user=request.user)
        product.delete()
        return HttpResponse(b"OK", status=200)
    
    return HttpResponseNotFound()