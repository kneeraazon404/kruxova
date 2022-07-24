#*****************************************
#IMPORTs python
#*****************************************

#*****************************************
#IMPORTs django
#*****************************************
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#*****************************************
#IMPORTs app
#*****************************************
from app_user import models as app_user_models

from app_user.api_routes.api_routes_crud import api_routes_crud_serializers

class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class= api_routes_crud_serializers.UserSerializer
    queryset = app_user_models.User.objects.all()

class ContactViewSet(viewsets.ModelViewSet):

    #permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class= api_routes_crud_serializers.ContactSerializer
    queryset = app_user_models.Contact.objects.all()