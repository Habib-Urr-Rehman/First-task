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
        required_fields = [
            "username", "email", "contact_number", "years_of_experience",
            "university_name", "degree_name", "password1"
        ]

        user_data = {field: request.POST.get(field) for field in required_fields}

        if not all(user_data.values()):
            messages.warning(request, 'Please fill in all the required fields')
            return redirect("/signup/")

        # Check for existing username and contact number
        existing_checks = {
            "username": user_data["username"],
            "contact_number": user_data["contact_number"]
        }

        for field, value in existing_checks.items():
            if CustomUser.objects.filter(**{field: value}).exists():
                messages.warning(request, f'{field.replace("_", " ").capitalize()} already exists')
                return redirect("/signup/")

        # Create and save the user object using dictionary unpacking
        CustomUser.objects.create(
            username=user_data["username"],
            email=user_data["email"],
            password=user_data["password1"],
            contact_number=user_data["contact_number"],
            years_of_experience=user_data["years_of_experience"],
            university_name=user_data["university_name"],
            degree_name=user_data["degree_name"]
        )

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

