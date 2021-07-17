from django.db.models import fields
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contact

class addcus(forms.ModelForm):
    class Meta:
        model = customer
        fields='__all__'

class add_to_cart(forms.ModelForm):
    class Meta:
        model = addtocart
        fields='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
#class signup(forms.ModelForm):
    class Meta:
        model = signup
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields='__all__'        