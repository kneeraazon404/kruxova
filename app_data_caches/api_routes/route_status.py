# ********************
# imports python
# ********************
import json

# **********************
# imports third-party
# **********************
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# ********************
# imports django
# ********************
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view,schema,permission_classes
from rest_framework.schemas import ManualSchema
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# ********************
# imports apps
# ********************
#models
from app_data_caches import models as app_data_caches_models

#********************************
# CUSTOM SCHEMA DEFINITIONS
#********************************
@swagger_auto_schema(
    operation_description='GET status of data caches',
    methods=['GET']
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def route(request):
    if request.method=="GET":
        
        response_data = list(
            app_data_caches_models.DataCacheStatus.objects.all().values()
        )

        #================================
        # SERIALIZE RESPONSE
        #================================
        data_serialized=json.dumps(response_data,default=str)
        return HttpResponse(data_serialized, content_type='application/json')
    else:
        #================================
        # SERIALIZE RESPONSE
        #================================
        data_serialized=json.dumps([])
        return HttpResponse(data_serialized, content_type='application/json')