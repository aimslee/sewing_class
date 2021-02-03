from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *
# from django.core.mail import send_mail


def index(request):
    # send_mail('from Django', 'This is an automated message from Amy', 'canvesgee@gmail.com', ['amy.star.lee@gmail.com'], fail_silently=False)
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def pay_page(request):
    return render(request, "pay_page.html")

def secure(request):
    return render(request, "secure.html")

#POST

def handle_registration(request):
    if request.method == 'POST':

        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, errors[error])
            return redirect ('/register')
    
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(8)).decode()
        new_user = User.objects.create(username = request.POST['username'], password = hashed_password)

        return redirect('/secure')
    return redirect('/register')



def handle_login(request):
    if request.method == 'POST':
        user_filtered_list = User.objects.filter(username = request.POST['username'])
        if len(user_filtered_list):
            existing_user = user_filtered_list[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), existing_user.password.encode()):
                return redirect('/secure')
        messages.error(request, 'Please enter a valid username and password')
        return redirect('/')
    return redirect('/')

# Create your views here.
