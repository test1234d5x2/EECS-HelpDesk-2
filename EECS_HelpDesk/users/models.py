from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPE_CHOICES = (
    ('student', 'Student'),
    ('ec_handler', 'EC Handler'),
    ('tech_fault_handler', 'Tech Fault Handler'),
    ('admin', 'Admin'),
)


# Create your models here.
class User(AbstractUser):
    user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES, default=USER_TYPE_CHOICES[0])
    email = models.EmailField(null=False)
    DOB = models.DateField(null=False)

    REQUIRED_FIELDS = ['email', 'DOB']