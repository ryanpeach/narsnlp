import os
from logger import *

log = createLogger("NARSInput", "./narsinput.txt")
    
class Nars():
    def __init__(self, path, include=[]):
        pass
    
    def process(self, inx):
        if isinstance(inx, iter):
            for x in inx:
                print(str(x))
                log.debug(str(x))
        else:
            print(str(inx))
            log.debug(str(inx))
            
    def quit(self):
        print("Quitting...")