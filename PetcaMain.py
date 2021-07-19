import numpy as np
from SecurityDomain import Info_Security as security
import discord
import key
import tempfile
import cv2
#...


class PetCam():

    def __init__(self):
        self.ky = key.app
        pass

    def picture_capture(self):
        for a in range(0,45):
            cap = cv2.VideoCapture(0)
            if a == 40:
                ret, frame = cap.read()
                with tempfile.TemporaryFile(suffix=".png") as tmpfile:
                    cv2.imwrite(tmpfile, frame)
                    tmpfile.seek(0) # Rewind the file. (0: the beginning of the file)
                    with open(tempfile,"rb") as f:
                        picture = discord.File(f)
                        return picture

    def requestreceiver(self):
        #if message there return True
        return False
    def main(self):
        client = discord.Client()
        listy = texts.text
        @client.event
        async def on_ready():
            print("Pet Camera Request Receiver Ready.")
        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            if security.password_check(message.content):
                picture = self.picture_capture()
                await message.channel.send(file=picture)

        client.run(key.app)


        #Camera Activation
        #...
        passlist = [] # passlist = read_config.ini or something
        requested = False
        password = ""
        secure = security()
        while True:
            #frame = "" #to get the frame from the webcam via opencv
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            with tempfile.TemporaryFile(suffix=".png") as tmpfile:
                cv2.imwrite(tmpfile, frame)
                tmpfile.seek(0) # Rewind the file. (0: the beginning of the file)
                with open(tempfile,"rb") as f:
                    picture = discord.File(f)
                    await channel.send(file=picture)
            #gather information

            requested = requestreceiver()     #this waits for the message to come.

            if requested == True:

                secure.password_check(password,passlist)
                #send the information to APP or discord, Whatever
                requested = False
                pass
