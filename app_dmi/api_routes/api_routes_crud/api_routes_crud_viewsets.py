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
from msdat_python_api_settings import settings_utils
from app_main import models as app_main_models

from app_dmi.api_routes.api_routes_crud import api_routes_crud_serializers

class DataViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = app_main_models.Data.objects.all()
    serializer_class= api_routes_crud_serializers.DataSerializer