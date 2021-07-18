import numpy as np
from SecurityDomain import Info_Security as security
#...


class PetCam():

    def __init__(self):
        pass

    def requestreceiver(self):
        #if message there return True
        return False
    def main(self):
        #Camera Activation
        #...
        passlist = [] # passlist = read_config.ini or something
        requested = False
        password = ""
        secure = security()
        while True:
            frame = "" #to get the frame from the webcam via opencv
            #gather information

            requested = requestreceiver()     #this waits for the message to come.

            if requested == True:

                secure.password_check(password,passlist)
                #send the information to APP or discord, Whatever
                requested = False
                pass
