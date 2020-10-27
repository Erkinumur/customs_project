from django.urls import path

from orders.views import ClientOrderListView, OrderDetail, OrderCreateView, \
    DriverOrderListView

urlpatterns = [
    path('orders/', ClientOrderListView.as_view(), name='client_orders'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='client_order'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/driver/', DriverOrderListView.as_view(),
         name='driver_orders'),
]