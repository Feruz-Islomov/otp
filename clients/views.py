from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,  UpdateView
from django.urls import reverse_lazy
from .models import Car, Order
from .utils import fetchAuthorCar, fetchAuthorOrder
from washers.models import Balance
from django.http import JsonResponse
import datetime
import json
import os
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only, driver_only
from accounts.mixins import MessageHandler

unauthenticated_user
def clientHomePage(request):
    
    context = {'name': 'Asus'}
    return render(request, 'client/homepage.html', context)
 
@login_required
@allowed_users(allowed_roles=['client', 'admin'])#/////////should be not_allowed//////////////
def orderPage(request):
    obj = fetchAuthorCar(request)
    context = {'cars': obj}
    return render(request, 'client/clientOrderPage.html', context)

class AddCar(LoginRequiredMixin, CreateView):
    model = Car
    fields = ('Model', 'Raqam', 'Rang', 'Photo')
    template_name = "client/car_add.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class CarEdit(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ('Model', 'Raqam', 'Rang')
    template_name = 'client/car_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

@login_required
def deleteCar(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
        if bool(car.Photo) == True and len(car.Photo) > 0:
            os.remove(car.Photo.path)
            car.delete()
            messages.success(request, 'car deleted succesfully.')
            return redirect('/client_profile')
    context = {'car': car}
    return render(request, 'client/car_delete.html', context)


class ClientCars(LoginRequiredMixin, DetailView):
    model = Car
    fields = ('Model', 'Raqam', 'Rang')
    template_name = "client/car.html" 

@login_required
def processOrder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        transaction_id = datetime.datetime.now().timestamp()
        customer = request.user
        carid = data['form']['carid']

        car = Car.objects.get(id=carid)
        Order.objects.create(
            customer=customer, 
            car=car,
            transaction_id = transaction_id,
            cost = data['form']['cost'],
            part = data['form']['part'],
            paytype = data['form']['paytype'],
            latitude = data['form']['latitude'],
            longitude = data['form']['longitude']
        )
    return JsonResponse('Payment submitted..', safe=False)
    
# this view is not shown for client
@login_required
@allowed_users(allowed_roles=['admin','driver'])
def clientOrders(request):
    orders = Order.objects.all()
    obj, created = Balance.objects.get_or_create(user=request.user)
    context = {'orders': orders, 'balance': obj}
    return render(request, 'client/orders.html', context)

# history should be one month limit
@login_required
@allowed_users(allowed_roles=['client'])
def clientOrderList(request):
    carts = fetchAuthorOrder(request)
    context = {'carts': carts['carts'], 'orders': carts['orders']}
    return render(request, 'client/client_order_list.html', context)

@login_required
def clientProfile(request):
    print('otp is pending clients view')
    MessageHandler('+966530867492', 477)
    obj = fetchAuthorCar(request)
    context = {'cars': obj}
    group = request.user.groups.all()[0].name
    if group == 'driver':
        return redirect('driverprofile')
    return render(request, 'client/clientProfile.html', context)




