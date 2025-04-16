# *****************************************
# IMPORTs python
# *****************************************
import os

# *****************************************
# IMPORTs shared
# *****************************************
from shared.utils import utils_logger

# *****************************************
# IMPORTs app
# *****************************************
from core.settings import utils

# *****************************************
# CHECK THE SET ENVIROMENT_VARIABLE
# *****************************************
# if enviroment variable not set use default ENV_LOCAL_SQLITE3
ENV_VAR_VALUE = os.environ.get(
    utils.ENV_VAR_KEY, utils.ENV_LOCAL_SQLITE3
)

# log
utils_logger.print_prety("ENVIROMENT SETTINGS", ENV_VAR_VALUE, param_oneline=False)

# import settings for env
if ENV_VAR_VALUE == utils.ENV_LOCAL_SQLITE3:
    from core.settings.local import *

elif ENV_VAR_VALUE == utils.ENV_LOCAL_PGSQL:
    from core.settings.local_pgsql import *

elif ENV_VAR_VALUE == utils.ENV_STAGING_SERVER_PGSQL:
    from core.settings.staging import *

elif ENV_VAR_VALUE == utils.ENV_PRO_SERVER_PGSQL:
    from core.settings.production import *

else:
    from core.settings.local import *
