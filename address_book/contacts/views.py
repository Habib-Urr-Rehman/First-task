from django.shortcuts import render, redirect
from contacts.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from contacts.models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html',{'contacts':contacts})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
            phone = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']

            email_content = f"Name: {name}\nPhone: {phone}\nAddress: {address}\nEmail: {email}"

            # Send the email
            send_mail(
                'New Contact Added',
                email_content,
                settings.EMAIL_HOST_USER,  # Sender's email address
                ['2021cs665@student.uet.edu.pk'],  # List of recipients
            )

         
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'add_contact.html', {'form': form})
