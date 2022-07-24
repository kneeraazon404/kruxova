# *****************************************
# IMPORTs django
# *****************************************
from django.urls import path, include
from rest_framework import routers

# *****************************************
# IMPORTs app
# *****************************************
from app_main.api_routes.api_routes_crud import (
    api_routes_crud_registry as app_main_api_routes_crud_registry,
)
from app_main.api_routes.api_routes_custom import (
    route_get_latest,
    route_get_by_location_level,
    route_get_after_datetime,
)

api_router_app_main = routers.DefaultRouter()
app_main_api_routes_crud_registry.register_routes(api_router_app_main)

urlpatterns = [
    # *****************************************
    # ROUTES crud(default) api routes
    # *****************************************
    path("crud/", include(api_router_app_main.urls)),
    # *****************************************
    # ROUTES custom api definitions
    # *****************************************
    path("data/latest/", route_get_latest.route, name="app_main_api_route_get_latest"),
    path(
        "data/location_level/<id>",
        route_get_by_location_level.route,
        name="app_main_api_route_get_by_location_level",
    ),
    path(
        "data/after_datetime/",
        route_get_after_datetime.route,
        name="app_main_api_route_get_after_datetime",
    ),
]
