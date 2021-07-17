import numpy as np
from SecurityDomain import Info_Security as security
#...


class PetCam():

    def __init__(self):
        pass

    def main(self):
        #Camera Activation
        #...
        passlist = [] # passlist = read_config.ini or something
        requested = False
        password = ""
        secure = security()
        while True:
            #gather information

            if requested == True:
                #send the information to APP or discord, Whatever
                secure.password_check(password,passlist)
                pass
