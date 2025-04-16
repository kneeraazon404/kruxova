# ********************
# imports python
# ********************

# **********************
# imports third-party
# **********************
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

# ********************
# imports django
# ********************
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# ********************
# imports app
# ********************
#utils
from shared.utils import utils_drf
#models
from apps.main import models as main_models

#******************************************
# CUSTOM REQUEST DEFINITION
#******************************************
req_param_path_offset = openapi.Parameter(
    'offset',
    openapi.IN_QUERY,
    description="query offset",
    type=openapi.TYPE_INTEGER
)

req_param_path_limit = openapi.Parameter(
    'limit',
    openapi.IN_QUERY,
    description="query limit",
    type=openapi.TYPE_INTEGER
)

class RequestSerializer(serializers.Serializer):
    offset = serializers.CharField()

    limit = serializers.CharField()

    class Meta:
        ref_name = "apps.main_get_data_request"

#******************************************
# CUSTOM RESPONSE SERIALIZER DEFINITION
#******************************************

#respose http 200 definition
class Response200Serializer(serializers.Serializer):
    data = {}

    class Meta:
        ref_name = "apps.main_get_data_response200"

#respose http 400 definition
class Response400Serializer(serializers.Serializer):
    error = serializers.CharField()

    class Meta:
        ref_name = "apps.main_get_data_response400"

#********************************
# CUSTOM SCHEMA DEFINITIONS
#********************************
@swagger_auto_schema(
    operation_description='GET action to pull data in dmi format',
    methods=['GET'],
    manual_parameters=[
        req_param_path_offset,
        req_param_path_limit
    ],
    responses={
        200:openapi.Response(
            'response description',
            Response200Serializer
        ),
        400:openapi.Response(
            'response description',
            Response400Serializer
        )
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def route(request):

    if request.method=="GET":

        #==================================
        #Validate request
        #==================================

        serializer_req = RequestSerializer(
            data={
                "offset": request.GET["offset"],
                "limit": request.GET["limit"]
            }
        )

        if serializer_req.is_valid():

            #==================================
            #get validated data
            #==================================

            valid_data_offset = serializer_req.validated_data['offset']

            valid_data_limit = serializer_req.validated_data['limit']

            queryset = {}
            if valid_data_offset==None and valid_data_offset==None:
                queryset = main_models.Data.objects.all()
            else:
                queryset = main_models.Data.objects.all()[int(valid_data_offset):int(valid_data_limit)]

            
                #SERIALIZE AND RETURN
                return utils_drf.helper_json_response(
                    Response200Serializer,
                    queryset.values()
                )

        else:
            #SERIALIZE AND RETURN
            return utils_drf.helper_json_response(
                Response400Serializer,
                {"error":serializer_req.errors}
            )

    else:
        #SERIALIZE AND RETURN
        return utils_drf.helper_json_response(
            Response400Serializer,
            {"error":"bad request"}
        )