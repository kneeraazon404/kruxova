#*****************************************
#IMPORTs python
#*****************************************

#*****************************************
#IMPORTs django
#*****************************************
from rest_framework import serializers
#*****************************************
#IMPORTs app
#*****************************************
from app_main import models as app_main_models

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = app_main_models.Data
        fields = '__all__'