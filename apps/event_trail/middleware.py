# ********************
# imports python
# ********************
import json

#*****************************************
#IMPORTs django
#*****************************************

#*****************************************
#IMPORTs app
#*****************************************
from apps.event_trail import models as event_trail_models

class TrailRequests(object):
    def __init__(self, get_response):

        self.get_response = get_response

        #=================================================
        # One-time configuration and initialization.
        #=================================================

    def __call__(self, request):

        #=================================================
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        #=================================================

        response = self.get_response(request)

        #=================================================
        # Code to be executed for each request/response after
        # the view is called.
        #=================================================

        if response.streaming:
            """
            not handling streaming
            """
            return response

        if request.method in ['DELETE','POST','PUT','PATCH']:
            if request.user.is_authenticated:

                #=====================================
                #COMPOSE REQUEST SAVE OBJ
                #=====================================
                new_req={}
                new_req["route"]=request.get_full_path()
                new_req["method"]=request.method
                new_req["meta"]=request.META

                if request.method=='GET':
                    new_req["query_params"]=request.GET.lists()
                if request.method=='POST':
                    new_req["query_params"]=request.POST.lists()

                #=====================================
                #COMPOSE RESPONSE SAVE OBJ
                #=====================================
                new_res={}
                new_res["status_code"]=response.status_code

                #=====================================
                #SAVE TRAIL
                #=====================================
                new_trail=event_trail_models.TrailRequest()
                new_trail.user=request.user
                new_trail.method=request.method
                new_trail.request=json.dumps(new_req,default=str)
                new_trail.response=json.dumps(new_res,default=str)
                new_trail.save()

        return response