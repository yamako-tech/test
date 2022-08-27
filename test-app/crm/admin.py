from django.contrib import admin
from . import models
from .models import HomeMessage


## Super-Admin (T-Mark)
admin.site.register(HomeMessage)