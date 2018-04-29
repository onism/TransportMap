import sys
import logging
import warnings
import numpy as np

# define the logger, For me , I do not need MPI support
__all__ =['LOG_LEVEL', 'logger']

LOG_LEVEL = logging.getLogger().getEffectiveLevel()
logger = logging.getLogger('TM.TransportMaps')
logger.propagate = False
ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%s(asctime)s %(levelname)s:(name)s:%(message)s',"%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)
logger.addHandler(ch)

def setLogLevel(level):
    import TM
    TM.LOG_LEVEL = level
    for lname, logger in logging.Logger.manager.loggerDict.items():
        if "TM." in ln:
            logger.setLevel(level)