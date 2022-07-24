# ********************
# imports python
# ********************
import json
# ********************
# imports django
# ********************
from django.conf import settings
# ********************
# imports libs
# ********************
from libs.utils import utils_logger
from libs.legacy_converters import convert_datasource_meta_test,\
    convert_indicator_meta_data_test,\
    convert_meta_data_test,\
    convert_master_sheet,\
    convert_estimates,\
    convert_lga
# ********************
# imports apps
# ********************
from app_main import models as app_main_models
from app_data_caches import models as app_data_caches_models

def change_status(paran_name,param_status,param_error=None):
    obj_exists,obj_created=app_data_caches_models.DataCacheStatus.objects.get_or_create(
        cache_name=paran_name,
        cache_type=app_data_caches_models.CHOICES_CACHE_TYPE_FILE,
        defaults={
            "status":app_data_caches_models.CHOICES_STATUS_INPROGRESS,
            "error":None
        }
    )
    if obj_created==False:
        obj_exists.status=param_status
        obj_exists.error=param_error
        obj_exists.save()

def refresh():
    """
    generate new caches and overwrite
    existing files
    """

    #run caches in order of time-taken

    #=====================================================
    #REFRESH DATA-CACHE
    #all_data
    #=====================================================
    try:

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_ALL_DATA,
            app_data_caches_models.CHOICES_STATUS_INPROGRESS
        )

        #GENERATE CACHE

        data_retrieved=list(
            app_main_models.Data.objects.all().select_related().values(
                "id",
                "indicator",
                "period",
                "location",
                "datasource",
                "value_type",
                "value"
            )
        )

        cache_all_data = "{}/{}.json".format(
            settings.MEDIA_ROOT,
            app_data_caches_models.CACHE_NAME_ALL_DATA
        )

        with open(cache_all_data,"w+") as write_file:
            json.dump(data_retrieved,write_file)

        #free up memory
        data_retrieved=[]

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_ALL_DATA,
            app_data_caches_models.CHOICES_STATUS_COMPLETED
        )

    except Exception as e:
        #LOG
        utils_logger.log_print("",str(e),param_oneline=True)

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_ALL_DATA,
            app_data_caches_models.CHOICES_STATUS_FAILED,
            str(e)
        )

    """
    #=====================================================
    #REFRESH DATA-CACHE
    #master_sheet
    #=====================================================

    try:

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_MASTER_SHEET,
            app_data_caches_models.CHOICES_STATUS_INPROGRESS
        )

        #GENERATE CACHE

        data_retrieved=convert_master_sheet.run_process()

        cache_file = "{}/{}.json".format(
            settings.MEDIA_ROOT,
            app_data_caches_models.CACHE_NAME_MASTER_SHEET
        )

        with open(cache_file,"w+") as write_file:
            json.dump(data_retrieved,write_file)

        data_retrieved=[]

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_MASTER_SHEET,
            app_data_caches_models.CHOICES_STATUS_COMPLETED
        )

    except Exception as e:
        #LOG
        utils_logger.log_print("",str(e),param_oneline=True)

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_MASTER_SHEET,
            app_data_caches_models.CHOICES_STATUS_FAILED,
            str(e)
        )

    #=====================================================
    #REFRESH DATA-CACHE
    #estimates_data
    #=====================================================

    try:

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_ESTIMATES_DATA,
            app_data_caches_models.CHOICES_STATUS_INPROGRESS
        )

        #GENERATE CACHE

        data_retrieved=convert_estimates.run_process()

        cache_file = "{}/{}.json".format(
            settings.MEDIA_ROOT,
            app_data_caches_models.CACHE_NAME_ESTIMATES_DATA
        )

        with open(cache_file,"w+") as write_file:
            json.dump(data_retrieved,write_file)

        data_retrieved=[]

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_ESTIMATES_DATA,
            app_data_caches_models.CHOICES_STATUS_COMPLETED
        )

    except Exception as e:
        #LOG
        utils_logger.log_print("",str(e),param_oneline=True)

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_ESTIMATES_DATA,
            app_data_caches_models.CHOICES_STATUS_FAILED,
            str(e)
        )

    #=====================================================
    #REFRESH DATA-CACHE
    #lga_data
    #=====================================================

    try:

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_LGA_DATA,
            app_data_caches_models.CHOICES_STATUS_INPROGRESS
        )

        #GENERATE CACHE

        data_retrieved=convert_lga.run_process()

        cache_file = "{}/{}.json".format(
            settings.MEDIA_ROOT,
            app_data_caches_models.CACHE_NAME_LGA_DATA
        )

        with open(cache_file,"w+") as write_file:
            json.dump(data_retrieved,write_file)

        data_retrieved=[]

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_LGA_DATA,
            app_data_caches_models.CHOICES_STATUS_COMPLETED
        )

    except Exception as e:
        #LOG
        utils_logger.log_print("",str(e),param_oneline=True)

        #SAVE STATUS
        change_status(
            app_data_caches_models.CACHE_NAME_LGA_DATA,
            app_data_caches_models.CHOICES_STATUS_FAILED,
            str(e)
        )
    """