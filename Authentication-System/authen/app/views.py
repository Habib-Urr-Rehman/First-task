from django.shortcuts import  redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import get_object_or_404 
from .models import CustomUser

@login_required
def home_page(request):
    users = CustomUser.objects.filter(is_superuser=False)
    return render(request, 'home.html', {'users': users})

def user_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        years_of_experience = request.POST.get("years_of_experience")
        university_name = request.POST.get("university_name")
        degree_name = request.POST.get("degree_name")
        password1 = request.POST.get("password1")
        
        # Check if all required fields are provided
        if not all([username, email, contact_number, years_of_experience, university_name, degree_name, password1]):
            messages.warning(request, 'Please fill in all the required fields')
            return redirect("/signup/")

        # Check if username already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already taken')
            return redirect("/signup/")

        # Check if contact number already exists
        if CustomUser.objects.filter(contact_number=contact_number).exists():
            messages.warning(request, 'Contact number already exists')
            return redirect("/signup/")

        # Create the user object
        user = CustomUser.objects.create(
            username=username,
            email=email,
            contact_number=contact_number,
            years_of_experience=years_of_experience,
            university_name=university_name,
            degree_name=degree_name
        )
        user.set_password(password1)  # Set the password
        user.save()

        messages.success(request, 'Account successfully created')
        return redirect("/home/")

    return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = authenticate(username=email, password=password)
            if not user:
                raise ValueError('Invalid email or password')  # Raise an exception if authentication fails

            login(request, user)
            messages.info(request, 'Login Successfully')
            return redirect("/home/")
        except ValueError as e:
            messages.warning(request, str(e))  # Display the exception message as a warning
            print(f"Authentication failed: {e}")

    return render(request, 'login.html')

