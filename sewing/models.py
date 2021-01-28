from django.db import models

class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        if len(post_data['username']) < 6 or len(post_data['username']) > 30:
            errors['username'] = 'Username must be between 6 and 30 characters long'
        if len(post_data['password']) < 6 or len(post_data['password']) > 30:
            errors['password'] = 'Password must be between 6 and 30 characters long'
        if post_data['password'] != post_data['confirm_password']:
            errors['password_match'] = 'Password fields do not match'
        return errors

class User(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

# class Product(models.Model):
#     class_name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     price = models.FloatField(null=True, blank=True)
#     customer = models.ForeignKey(customer, on_delete=models.CASCADE)

# class Customer(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
