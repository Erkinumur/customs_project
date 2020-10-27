from django.shortcuts import render
from django.views import generic

from admin_panel.models import Order


class ClientOrderListView(generic.ListView):
    model = Order
    template_name = 'orders/client_order_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(owner=user.client)
        return queryset


class OrderDetail(generic.DetailView):
    model = Order
    template_name = 'orders/client_order_detail.html'

