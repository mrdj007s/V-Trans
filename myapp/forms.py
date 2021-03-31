from django import forms
from .models import (
    signup,
    bookvehicle,
    proceed,
    contactus,
    payment
)
from .models import trucks
from .models import driver
from .models import summary

class SignupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

class BookvehicleForm(forms.ModelForm):
    class Meta:
        model=bookvehicle
        fields='__all__'

class ProceedForm(forms.ModelForm):
    class Meta:
        model=proceed
        fields='__all__'

class summaryForm(forms.ModelForm):
    class Meta:
        model=proceed
        fields='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model=contactus
        fields='__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model=payment
        fields='__all__'

class TrucksForm(forms.ModelForm):
    class Meta:
        model=trucks
        fields='__all__'

class DriverForm(forms.ModelForm):
    class Meta:
        model=driver
        fields='__all__'