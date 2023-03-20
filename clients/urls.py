from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientHomePage, name='clientHomePage'),
    path('order/', views.orderPage, name='order'),
    path('orders/', views.clientOrders, name='orders'),
    path('client_order_list/', views.clientOrderList, name='order_list'),
    path('client_profile/', views.clientProfile, name='clientprofile'),
    path('client_profile/add_car/', views.AddCar.as_view(), name='addcar'),
    path('client_profile/edit_car/<slug:pk>/', views.CarEdit.as_view(), name='editcar'),
    path('client_profile/client_cars/<slug:pk>/', views.ClientCars.as_view(), name='clientcars'),
    path('client_profile/del_car/<slug:pk>', views.deleteCar, name='deletecar'),
    path('process_order/', views.processOrder, name="process_order"),
]
# path('order/confirm/', views.orderConfirm, name='confirm'),