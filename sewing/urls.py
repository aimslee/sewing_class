from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    path('handle_registration', views.handle_registration),
    path('sign_up', views.sign_up),
    path('pay_page', views.pay_page, name='pay_page'),
]