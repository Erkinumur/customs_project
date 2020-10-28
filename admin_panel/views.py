from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate
from .models import *
from .forms import WorkerForm, DriverForm, SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('1')
            Client.objects.create(user=user, organization=form.cleaned_data['organization'],
            inn=form.cleaned_data['inn'], address=form.cleaned_data['address'],
            okpo=form.cleaned_data['okpo'])
            login(request, user)
            if user.is_staff:
                return redirect('orders')
            else:
                return redirect('client_orders')
        else:
            return render(request, 'signup.html', {'form':form})
    form = SignUpForm()
    return render(request, 'signup.html', locals())


def worker_create(request):
    if request.method == 'POST':
        if request.user.is_staff:
            form = WorkerForm(request.POST)
            if form.is_valid():
                user = form.save()
                Worker.objects.create(user=user, organization=form.cleaned_data['organization'],
                phone=form.cleaned_data['phone'],passport_id=form.cleaned_data['passport_id'],place=form.cleaned_data['place'])
                return redirect('workers')
            else:
                return render(request, 'worker_create.html', {'form': form})
    form = WorkerForm()
    return render(request, 'worker_create.html', locals())


def driver_create(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            user = form.save()
            Driver.objects.create(user=user, car_number=form.cleaned_data['car_number'],
            category=form.cleaned_data['category'], car_model=form.cleaned_data['car_model'],
            year_of_issue=form.cleaned_data['year_of_issue'],
            color=form.cleaned_data['color'], chassis=form.cleaned_data['chassis'],
            body_type=form.cleaned_data['body_type'], engine_power=form.cleaned_data['engine_power'],
            engine_type=form.cleaned_data['engine_type'])
            return redirect('drivers')
        form = form.errors
    form = DriverForm()
    return render(request, 'driver_create.html', locals())


def desinfection_client(request):
    if not request.user.is_staff:
        orders = Order.objects.filter(owner__user=request.user)
        return render(request, 'desinfection2.html', locals())
    else:
        return redirect('orders')
    



class OrdersView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'


class ClientsView(generic.ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients'


class DriversView(generic.ListView):
    model = Driver
    template_name = 'drivers.html'
    context_object_name = 'drivers'


class WorkersView(generic.ListView):
    model = Worker
    template_name = 'workers.html'
    context_object_name = 'workers'


class DesinfectionView(generic.ListView):
    model = Order
    template_name = 'desinfection.html'
    context_object_name = 'orders'


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return reverse('orders')
        try:
            client = user.client
            return reverse('client_orders')
        except:
            pass
        try:
            worker = user.worker
            return reverse('worker')
        except:
            pass
        try:
            driver = user.driver
            return reverse('driver_orders')
        except:
            return ''


def index(request):
    user = request.user
    try:
        client = user.client
        return redirect('client_orders')
    except:
        pass
    try:
        worker = user.worker
        return redirect('worker')
    except:
        pass
    try:
        driver = user.driver
        return redirect('driver_orders')
    except:
        return redirect('login')


class WorkerView(generic.ListView):
    model = Driver
    template_name = 'worker.html'

    def get_queryset(self):
        car_number = self.request.GET.get('car_number')
        queryset = Driver.objects.filter(car_number=car_number)
        return queryset


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = 'driver_detail.html'

    def post(self, request, *args, **kwargs):
        driver = self.get_object()
        approved = self.request.POST.get('approved')
        if approved:
            order = driver.orders.all().last()
            order.approved = True
            order.save()
        return redirect('worker')


class WorkerDetailView(generic.DetailView):
    model = Worker
    template_name = 'worker_detail.html'


def main(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    return redirect('login')