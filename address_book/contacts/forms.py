from django import forms
from django.core.validators import RegexValidator
from contacts.models import Contact

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
            # Check if any contact with this phone number exists
            contacts = Contact.objects.filter(phone_number=phone_number)
            if contacts.exists():
                # If editing an existing contact, allow the same phone number
                if self.instance and self.instance.pk in contacts.values_list('pk', flat=True):
                    return phone_number
                raise forms.ValidationError("This phone number already exists.")
            return phone_number
        except Contact.DoesNotExist:
            return phone_number
