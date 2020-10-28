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
        form = WorkerForm(request.POST)
        if form.is_valid():
            user = form.save()
            Worker.objects.create(user=user, organization=form.cleaned_data['organization'],
            phone=form.cleaned_data['phone'],passport_id=form.cleaned_data['passport_id'],place=form.cleaned_data['place'])
            if user.is_staff:
                return redirect('workers')
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
