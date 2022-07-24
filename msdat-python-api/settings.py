# *****************************************
# IMPORTs python
# *****************************************
import os

# *****************************************
# IMPORTs libs
# *****************************************
from libs.utils import utils_logger

# *****************************************
# IMPORTs app
# *****************************************
from msdat_python_api_settings import settings_utils

# *****************************************
# CHECK THE SET ENVIROMENT_VARIABLE
# *****************************************
# if enviroment variable not set use default ENV_LOCAL_SQLITE3
ENV_VAR_VALUE = os.environ.get(
    settings_utils.ENV_VAR_KEY, settings_utils.ENV_LOCAL_PGSQL
)

# log
utils_logger.print_prety("ENVIROMENT SETTINGS", ENV_VAR_VALUE, param_oneline=False)

# import settings for env
if ENV_VAR_VALUE == settings_utils.ENV_LOCAL_SQLITE3:
    from msdat_python_api_settings.settings_local_sqlite3 import *

elif ENV_VAR_VALUE == settings_utils.ENV_LOCAL_PGSQL:
    from msdat_python_api_settings.settings_local_pgsql import *

elif ENV_VAR_VALUE == settings_utils.ENV_STAGING_SERVER_PGSQL:
    from msdat_python_api_settings.settings_staging_pgsql import *

elif ENV_VAR_VALUE == settings_utils.ENV_PRO_SERVER_PGSQL:
    from msdat_python_api_settings.settings_pro_pgsql import *

else:
    from msdat_python_api_settings.settings_local_sqlite3 import *
