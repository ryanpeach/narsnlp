import logging
import sys
import os

def createLogger(name,path,level=None,out=False):
    logger = logging.getLogger(name)
    if len(logger.handlers) == 0:
        createPath(path,logger)
        filepath = path + logger.name + '.log'
        log = logging.FileHandler(filepath, mode='w')
        if level is not None:
            logger.setLevel(level)
            log.setLevel(level)
        else:
            logger.setLevel("DEBUG")
            log.setLevel("DEBUG")
        sform = logging.Formatter(fmt='%(levelname)s:\t%(processName)s:\t%(asctime)s:\t%(funcName)s:\t%(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        log.setFormatter(sform)
        logger.addHandler(log)
        if out:
            ch = logging.StreamHandler(sys.stdout)
            if level is not None:
                ch.setLevel(level)
            else:
                ch.setLevel("DEBUG")
            pform = logging.Formatter(fmt='%(message)s')
            ch.setFormatter(pform)
            logger.addHandler(ch)
    return logger

def createPath(path,logger):
    """ Creates path and subpaths, with logging and status return. """
    try:
        if os.makedirs(path):
            #logger.debug("Path created: {0}".format(path))
            return True
    except:
        if os.path.isdir(path):
            #logger.debug("Path already exists: {0}".format(path))
            return True
        else:
            logger.error("Path not created: {0}".format(path))
            return False

def createFile(path,logger):
    """ Creates path and subpaths, with logging and status return. """
    try:
        if os.makedirs(path):
            logger.debug("Path created: {0}".format(path))
            return True
    except:
        if os.path.isdir(path):
            logger.debug("Path already exists: {0}".format(path))
            return True
        else:
            logger.warning("Path not created: {0}".format(path))
            return False