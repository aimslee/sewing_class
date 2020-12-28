from django.shortcuts import render, redirect
from django.core.mail import send_mail

def index(request):
    # send_mail('from Django', 'This is an automated message from Amy', 'canvesgee@gmail.com', ['amy.star.lee@gmail.com'], fail_silently=False)
    return render(request, "send/index.html")

def sign_up(request):
    print(request.POST)
    return render(request, "send/pay_page.html")


# Create your views here.
