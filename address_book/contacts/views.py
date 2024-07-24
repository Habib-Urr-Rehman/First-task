from django.shortcuts import render
from django.shortcuts import  redirect
from contacts.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from contacts.models import Contact
import os

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html',{'contacts':contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}" #ref .https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/
            phone = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            email_content = f"Name: {name}\nPhone: {phone}\nAddress: {address}\nEmail: {email}"

            # Fetch environment variables
            sender_email = os.getenv('EMAIL_HOST_USER')
            recipient_email = os.getenv('EMAIL_RECIPIENT')

            # Send the email         # ref.https://docs.djangoproject.com/en/5.0/topics/email/
            send_mail(
                'New Contact Added',
                email_content,
                sender_email,  
                [recipient_email],  # List of recipients from environment variable
            )
         
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'add_contact.html', {'form': form})

