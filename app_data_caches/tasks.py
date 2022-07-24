# ********************
# imports vendors
# ********************
from celery import shared_task
# ********************
# imports libs
# ********************
from libs.data_caching import cache_to_files

@shared_task
def task_update_data_caches():
    """
    run action_save_data
    """
    cache_to_files.refresh()