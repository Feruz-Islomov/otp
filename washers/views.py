from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Driver_cart_order
from clients.models import Order, Car
from .utils import fetchDriverCart
import json
from django.contrib import messages
from django.http import JsonResponse
from clients.decorators import allowed_users
from django.shortcuts import redirect
from .models import Balance
from accounts.models import CustomUser

@login_required
@allowed_users(allowed_roles=['driver'])
def driver_profile(request):
    cart = fetchDriverCart(request)
    t = 0
    for x in cart:
        t = t + (x.cost/2)
    obj, created = Balance.objects.get_or_create(user=request.user)
    context = {'balance': obj, 't':t}
    return render(request, 'driver/driverProfile.html', context)

@login_required
@allowed_users(allowed_roles=['driver'])
def process_cart(request):
    if request.method == 'POST':
        driver = request.user
        data = json.loads(request.body)
        existItem = Order.objects.filter(id = data['form']['id']).exists()
        if existItem == True:
            obj, created = Balance.objects.get_or_create(user=driver)
            # obj.balance = 76000
            order = Order.objects.get(id = data['form']['id'])
            if obj.balance >= order.cost/2:
                order.delete()
                car = Car.objects.get(id = order.car.id)
                obj.balance = (obj.balance - (order.cost/2))
                obj.save()
                Driver_cart_order.objects.create(
                    driver = driver,
                    car = car,
                    ordered_by = order.customer.id,
                    cost = order.cost,
                    part = order.part,
                    paytype = order.paytype,
                    latitude = order.latitude,
                    longitude = order.longitude,
                )
                return JsonResponse('Buyurtmani tanladingiz!', safe=False)
            else:
                return JsonResponse('Hisobingiz yetarli emas!', safe=False)
        else:
            return JsonResponse('Buyurtma mavjud emas keyingisini tanlang!', safe=False)


@login_required
@allowed_users(allowed_roles=['driver'])
def finish_process(request, pk):
    order = Driver_cart_order.objects.get(id=pk)
    print('service is: ', order.service)
    if request.method == 'POST':
        order.service = Driver_cart_order.FINISHED
        Driver_cart_order.save()
    order.service = Driver_cart_order.FINISHED
    order.save()
    print('service is: ', order.service)
    return redirect('orders')



@login_required
@allowed_users(allowed_roles=['driver'])
def driverOrderList(request):
    obj, created = Balance.objects.get_or_create(user=request.user)  
    cart = fetchDriverCart(request)
    
    print(cart)
    context = {'carts': cart, 'balance': obj}
    return render(request, 'driver/driver_order_list.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def adminpage(request):
    obj = CustomUser.objects.all()
    # all_list = []
    client_list = []
    driver_list = []
    for client in obj:
        # n = client.groups.all()[0].name
        # all_list.append(n) 
        if client.groups.all()[0].name == 'client':
            client_list.append(client)
        else:
            driver_list.append(client)
    # nclient = all_list.count('client')
    # ndriver = all_list.count('driver')
    nclient = len(client_list)
    ndriver = len(driver_list)

    waiting = Order.objects.all()
    pending = Driver_cart_order.objects.filter(service='pending')
    finished = Driver_cart_order.objects.filter(service='finished')
    totals = Driver_cart_order.objects.all()
    total_sum = 0
    for total in totals:
        total_sum = total_sum + total.cost
    staff_sum = total_sum/2
    # print(total_sum)
    context = {'staffs': driver_list, 'clients': client_list, 'nclient':nclient, 'ndriver':ndriver, 'waiting':waiting.__len__(), 'pending':pending.__len__(), 'finished':finished.__len__(), 'total_sum':total_sum, 'staff_sum':staff_sum}
    return render(request, 'admin/admin_page.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def staff_balancing_input(request, pk):
    if request.method == 'POST':
        t = request.POST.get('balance')
        staff = CustomUser.objects.get(id=pk)
        obj, created = Balance.objects.get_or_create(user=staff)
        obj.balance = obj.balance + int(t)
        obj.save()
        messages.success(request, 'successfully added!')
        return redirect('admin_page')
    context={}
    return render(request, 'admin/balancing.html', context)
