from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):

    first_name  =  forms.CharField(widget=forms.TextInput(attrs={'class' : "form-control"}))
    last_name  =  forms.CharField(widget=forms.TextInput(attrs={'class' : "form-control"}))
    email  =  forms.CharField(widget=forms.TextInput(attrs={'class' : "form-control"}))
    address  =  forms.CharField(widget=forms.TextInput(attrs={'class' : "form-control"}))
    phone  =  forms.CharField(widget=forms.TextInput(attrs={'class' : "form-control"}))
    order_notes  =  forms.CharField(widget=forms.Textarea(attrs={'class' : "form-control", 'placeholder' : "Notes about your order, e.g. special notes for delivery."}))

    class Meta:
        model = Order
        fields = '__all__'

