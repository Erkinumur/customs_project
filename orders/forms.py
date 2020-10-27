from django import forms

from admin_panel.models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'login',
            'placeholder': self.fields['name'].label})
        self.fields['receiver'].widget.attrs.update({
            'class': 'login',
            'placeholder': self.fields['receiver'].label})
        self.fields['invoice'].widget.attrs.update({
            'class': 'login',
            'placeholder': self.fields['invoice'].label})
        self.fields['packing_list'].widget.attrs.update({
            'class': 'login',
            'placeholder': self.fields['packing_list'].label})

    class Meta:
        model = Order
        exclude = ['owner', 'driver']
