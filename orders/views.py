from django.core import exceptions
from django.shortcuts import render, redirect
from django.views import generic

from admin_panel.models import Order, Client
from orders.forms import OrderCreateForm


class ClientOrderListView(generic.ListView):
    model = Order
    template_name = 'orders/client_order_list.html'

    def get_queryset(self):
        user = self.request.user
        try:
            user.client
            queryset = Order.objects.filter(owner=user.client)
        except:
            try:
                driver = user.driver
                queryset = Order.objects.filter(driver__isnull=True)
                self.template_name = 'orders/driver_order_list.html'
            except:
                queryset = []
        return queryset


class OrderDetail(generic.DetailView):
    model = Order
    template_name = 'orders/client_order_detail.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            driver = user.driver
            self.template_name = 'orders/driver_order_detail.html'
        except:
            pass
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            driver = user.driver
            obj = self.get_object()
            obj.driver = driver
            obj.save()
            return redirect(obj.get_absolute_url())
        except:
            pass


class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/order_create.html'

    def post(self, request, *args, **kwargs):
        self.object = None
        user = request.user
        client = user.client
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = client
            obj.save()
            return redirect(obj.get_absolute_url())
        return self.render_to_response(self.get_context_data(form=form))


class DriverOrderListView(generic.ListView):
    model = Order
    template_name = 'orders/driver\'s_order_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(driver=user.driver)
        return queryset
