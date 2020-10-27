from django.urls import path

from orders.views import ClientOrderListView, OrderDetail

urlpatterns = [
    path('orders', ClientOrderListView.as_view(), name='client_orders'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='client_order')
]