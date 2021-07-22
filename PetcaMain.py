import numpy as np
from SecurityDomain import Info_Security as security
import discord
import key
import tempfile
import cv2
from PIL import Image
import os
from PetUtils import PetUtils
#...


class PetCam():

    def __init__(self):
        self.ky = key.app
        PetUtils().create_folder_if_None_exists("Nekos")
        pass

    def picture_capture(self):
        cap = cv2.VideoCapture(0)
        for a in range(0,45):
            ret, frame = cap.read()
            if a == 40:
                #ret, frame = cap.read()
                cv2.imwrite(os.path.join("Nekos","temp2send.png"), frame)
                with open(os.path.join("Nekos","temp2send.png"),"rb") as f:
                    picture = discord.File(f)
                    return picture

    def main(self):
        client = discord.Client()
        @client.event
        async def on_ready():
            print("Pet Camera Request Receiver Ready.")
        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            else:
                await message.channel.send("はい")
            if security().password_check(message.content,key.passlist):
                if str(message.author) in key.allowedusers:
                    await message.channel.send("{}様:heart_eyes_cat:カメラ用意します!!".format(str(message.author)[0:-5]))
                    picture = self.picture_capture()
                    await message.channel.send(file=picture)
                else:
                    await message.channel.send("{}:smirk_cat:君はダメにゃ:joy_cat:".format(str(message.author)[0:-5]))

        client.run(key.app)

if __name__ == "__main__":
    PC = PetCam()
    PC.main()
