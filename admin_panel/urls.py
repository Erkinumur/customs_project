from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView



urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('clients/', ClientsView.as_view(), name='clients'),
    path('workers/', WorkersView.as_view(), name='workers'),
    path('drivers/', DriversView.as_view(), name='drivers'),
    path('desinfection/', DesinfectionView.as_view(), name='desinfection'),
    path('desinfection_client/', desinfection_client, name='desinfection_client'),
    path('worker_create/', worker_create, name='worker_create'),
    path('driver_create/', driver_create, name='driver_create'),
    path('signup/', signup, name='signup'),
]