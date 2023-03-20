from django.urls import path
from . import views


urlpatterns =[
    path('signup/', views.registerPage, name='signup'),
    path('edit-profile/<int:pk>/', views.clientProfileEdit, name='editprofile'),
]