
from datetime import datetime
import logging
import os
import sys 


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # log file name example: 08_22_2000_12_00_00.log 

# create a path to the log file 

LOG_PATH = os.path.join(os.getcwd(), "logs",LOG_FILE) # create a path to the log file 

os.makedirs(LOG_PATH , exist_ok=True) # create the log file example: C:\Users\AGRAT_MOHAMMED\ML_project\logs\08_22_2000_12_00_00.log


LOG_FILE_PATH = os.path.join(LOG_PATH , LOG_FILE) 


logging.basicConfig( # configure the log file 
                
    filename=LOG_FILE_PATH, # log file path
    
    format = "[%(asctime)s] %(lineno)d:%(name)s:%(levelname)s:%(message)s", # log format example: [08/22/2000 12:00:00] 1:main:INFO:log message
    
    level = logging.INFO , # log level example: INFO , DEBUG , WARNING , ERROR , CRITICAL , NOTSET ....
    

)

