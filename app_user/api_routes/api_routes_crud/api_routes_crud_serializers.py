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
from app_user import models as app_user_models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = app_user_models.User
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = app_user_models.Contact
        fields = '__all__'