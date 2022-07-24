#******************************************
#IMPORTS python
#******************************************

#******************************************
#IMPORTS django
#******************************************
from django.contrib import admin
from app_main import models as app_main_models

class Admin_Model_Data(admin.ModelAdmin):

    list_display=(
        'id',
        'indicator',
        'datasource',
        'location',
        'value_type',
        'period',
        'value',
        'created_at',
        'updated_at'
    )

    list_filter=(
        'indicator',
        'datasource',
        'value_type',
        'period',
        'created_at',
        'updated_at'
    )