from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'person_number','order_begin_date', 'order_end_date', 'order_note']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'person_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Person Number'}),
            'order_begin_date': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'placeholder': 'Order Begin Date','type': 'date'}),
            'order_end_date': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'placeholder': 'Order End Date','type': 'date'}),
            'order_note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Order Note'}),
            
            
}

        