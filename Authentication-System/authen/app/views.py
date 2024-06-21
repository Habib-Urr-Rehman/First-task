from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
import re


def signup(request):
    if request.method == "POST":
        e = request.POST.get("email")
        p1 = request.POST.get("pass1")
        p2 = request.POST.get("pass2")

        # Validate email 
        email_regex = r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'
        if not re.match(email_regex, e):
            messages.error(request, 'Invalid email address')
            return redirect("/signup/")

        # Validate password against the regex
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
        if not re.match(password_regex, p1):
            messages.error(request, 'Password must be at least 8 characters long and include at least one lowercase letter, one uppercase letter, one digit')
            return redirect("/signup/")

        if p1 != p2:
            messages.info(request, 'Passwords do not match')
            return redirect("/signup/")

        # Check if email already exists
        try:
            User.objects.get(username=e)
            messages.warning(request, 'Email already taken')
            return redirect("/signup/")
        except User.DoesNotExist:
            pass

        # Create new user
        myuser = User.objects.create_user(username=e, email=e, password=p1)
        myuser.save()
        messages.success(request, 'Account successfully created')
        return redirect("/login/")

    return render(request, 'signup.html', {})



def userlogin(request):
    if request.method == "POST":
        get_email = request.POST.get("emaill")
        get_password= request.POST.get("pass")

        myuser = authenticate(username=get_email, password=get_password)

        if myuser is not None:
            login(request, myuser)
            messages.success(request,'Login Successfully')
        
            return redirect("/home/") 
        else:
            messages.warning(request, 'Invalid username or password')

    return render(request,'login.html',{})



def homepage(request):
    
    return render(request,'home.html',{})