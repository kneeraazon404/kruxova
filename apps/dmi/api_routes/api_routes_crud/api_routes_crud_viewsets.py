#*****************************************
#IMPORTs python
#*****************************************

#*****************************************
#IMPORTs django
#*****************************************
from rest_framework import viewsets,status,pagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#*****************************************
#IMPORTs app
#*****************************************
from core.settings import utils
from apps.main import models as main_models

from apps.dmi.api_routes.api_routes_crud import api_routes_crud_serializers

class DataViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = main_models.Data.objects.all()
    serializer_class= api_routes_crud_serializers.DataSerializer