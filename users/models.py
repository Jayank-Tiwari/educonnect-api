from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's default User.
    Adds role-based fields for professors and students.

    This inherits all default fields:
    - username
    - password
    - email
    - first_name
    - last_name
    - is_active
    - date_joined
    """
    is_professor = models.BooleanField(
        default=False,
        help_text="Designates whether this user is a professor."
    )

    is_student = models.BooleanField(
        default = True,
        help_text = "Designates whether this user is a student."
    )
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
