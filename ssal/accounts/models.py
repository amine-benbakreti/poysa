from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager): #mas2oula 3la creating user win noverridou methods tewwe3ha
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser): #hadi user model bi nafseh nmodifouh 
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)

    objects = CustomUserManager() 
    # overrides the default manager (objects) for the User model 
    # with a custom manager called CustomUserManager. This means that 
    # instances of the User model will be managed using the methods defined 
    # in the CustomUserManager class instead of the default manager provided by Django.

    USERNAME_FIELD = "email" # This specifies the field used for authentication
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username



# User (Custom User Model):
# This is the representation of a user object in your Django application.
# It defines the structure of the user model, including its fields and behaviors.
# You use the User model to interact with user data in your application, such as creating, updating, and deleting users.
# In the provided code, the User model inherits from AbstractUser and adds custom fields (email, username, date_of_birth) specific to your application's requirements.
# CustomUserManager:

# This is a custom manager class responsible for creating and managing instances of the custom user model (User).
# It extends BaseUserManager, a Django-provided class for managing user creation.
# The CustomUserManager class overrides methods like create_user and create_superuser, allowing you to customize the user creation process.
# You use CustomUserManager to create user instances with specific attributes or conditions, such as creating regular users or superusers with predefined settings.
# It encapsulates the logic for creating user instances and can be customized to fit your application's authentication requirements, such as email normalization or setting default permissions for superusers.