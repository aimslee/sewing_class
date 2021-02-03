from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    path('handle_registration', views.handle_registration),
    path('secure', views.secure),
    path('handle_login', views.handle_login),
    # path('handle_logout', views.handle_logout),
    path('pay_page', views.pay_page, name='pay_page'),
]