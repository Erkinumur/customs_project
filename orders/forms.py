from django import forms

from admin_panel.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['owner', 'driver']
