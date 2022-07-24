#*****************************************
#IMPORTs python
#*****************************************
import os

#*****************************************
#IMPORTs django
#*****************************************
from django.contrib import admin

#*****************************************
#IMPORTs libs
#*****************************************

#*****************************************
#IMPORTs app
#*****************************************
from app_user import models

# Register your models here.
admin.site.register(models.User)

admin.site.register(models.Contact)