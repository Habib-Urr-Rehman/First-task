from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import CustomUser
from django.http import JsonResponse

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        years_of_experience = request.POST.get("years_of_experience")
        university_name = request.POST.get("university_name")
        degree_name = request.POST.get("degree_name")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        try:
            CustomUser.objects.get(username=username)
            messages.warning(request, 'Username already taken')
            return redirect("/signup/")
        except CustomUser.DoesNotExist:
            pass

        user = CustomUser.objects.create_user(username=username, email=email, password=password1,
                                              contact_number=contact_number, years_of_experience=years_of_experience,
                                              university_name=university_name, degree_name=degree_name)
        user.save()
        messages.success(request, 'Account successfully created')
        return redirect("/home/")

    return render(request, 'signup.html')


def userlogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Login Successfully')
            return redirect("/home/")
        else:
            print("Authentication failed")
            messages.warning(request, 'Invalid email or password')

    return render(request, 'login.html')

def homepage(request):
  
      
        users = CustomUser.objects.filter(is_superuser=False)
        return render(request, 'home.html', {'users': users})
    
