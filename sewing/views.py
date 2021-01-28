from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# import bcrypt

def index(request):
    # send_mail('from Django', 'This is an automated message from Amy', 'canvesgee@gmail.com', ['amy.star.lee@gmail.com'], fail_silently=False)
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def sign_up(request):
    print(request.POST)
    password = request.POST['password']
    # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # print(pw_hash)
    # User.objects.create(username=request.POST['username'], password=pw_hash)
    return redirect('pay_page')

def pay_page(request):
    return render(request, "pay_page.html")

#POST

def handle_registration(request):
    pass

# Create your views here.
