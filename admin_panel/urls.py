from django.urls import path
from .views import *


urlpatterns = [
    path('orders/', OrdersView.as_view()),
    path('clients/', ClientsView.as_view()),
    path('workers/', WorkersView.as_view()),
    path('drivers/', DriversView.as_view()),
    path('worker_create/', worker_create, name='worker_create'),
    path('driver_create/', driver_create, name='driver_create'),
]