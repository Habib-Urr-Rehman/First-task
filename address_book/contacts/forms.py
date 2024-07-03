from django import forms
from django.core.validators import RegexValidator
from contacts.models import Contact
from django.shortcuts import get_object_or_404

class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, validators=[
        RegexValidator(r'^\d{1,15}$', message="Phone number must be numeric.")
    ])

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

def clean_phone_number(self):
    phone_number = self.cleaned_data['phone_number']
    try:
        contact = get_object_or_404(Contact, phone_number=phone_number)
        if self.instance and self.instance == contact:
            return phone_number
        raise forms.ValidationError("This phone number already exists.")
    except Contact.DoesNotExist:
        return phone_number