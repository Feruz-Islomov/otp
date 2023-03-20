from django.urls import path
from . import views

urlpatterns = [
    path('driver_profile/', views.driver_profile, name='driverprofile'),
    path('driver_cart/', views.process_cart, name='process_cart'),
    path('driver_order_list/', views.driverOrderList, name='driver_order_list'),
    path('driver_order_list/<slug:pk>', views.finish_process, name='finish_cart'),
    path('admin_page/', views.adminpage, name='admin_page'),
    path('balance_form/<slug:pk>', views.staff_balancing_input, name='balance_form'),
]
