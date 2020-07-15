# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

    CLIENT = 'CL'
    EXPERT = "EX"
    EMPLOYEE = "EM"
    type_user = [
        (CLIENT,'CLIENT'),
        (EXPERT,'EXPERT'),
        (EMPLOYEE,'EMPLOYEE')
    ]
    user_type = models.CharField(
        max_length=10,
        choices=type_user,
        default=CLIENT
    )