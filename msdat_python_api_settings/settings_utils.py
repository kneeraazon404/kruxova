#*****************************************
#IMPORTs python
#*****************************************
import os
#*****************************************
#IMPORTs libs
#*****************************************

#*****************************************
#IMPORTs app
#*****************************************

#!!!NOTE
#use this as the enviroment variable NAME
ENV_VAR_KEY="E4E_ENVVAR_MSDATAPI_ENV"

#!!!NOTE
#this are the available values for the enviroment variable
ENV_LOCAL_SQLITE3="ENV_LOCAL_SQLITE3"

ENV_LOCAL_PGSQL="ENV_LOCAL_PGSQL"

ENV_STAGING_SERVER_PGSQL="ENV_STAGING_SERVER_PGSQL"

ENV_PRO_SERVER_PGSQL="ENV_PRO_SERVER_PGSQL"

def helper_check_env_is_pro():
    """
    check if the deployment enviroment is production

    Args:

    Returns:
        :rtype:bool
    """
    #get the env_var
    env_var_value=os.environ.get(ENV_VAR_KEY,None)

    if (env_var_value == ENV_PRO_SERVER_PGSQL):
        return True
    else:
        return False

def helper_check_env_is_staging():
    """
    check if the deployment enviroment is staging

    Args:

    Returns:
        :rtype:bool
    """
    #get the env_var
    env_var_value=os.environ.get(ENV_VAR_KEY,None)

    if (env_var_value == ENV_STAGING_SERVER_PGSQL):
        return True
    else:
        return False

def helper_check_env_is_local():
    """
    check if the deployment enviroment is local/dev

    Args:

    Returns:
        :rtype:bool
    """
    #get the env_var
    env_var_value=os.environ.get(ENV_VAR_KEY,None)

    if (env_var_value == ENV_LOCAL_SQLITE3) or (env_var_value == ENV_LOCAL_PGSQL):
        return True
    else:
        return False