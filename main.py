import tkinter as tk
from TTS_Parser import TTV_Websocket
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from Components.auth.Login import Login
from Components.auth.Auth import checkData
import asyncio
import logging

class MainUI(tk.Frame):

    def __init__(self):
        self.loop = asyncio.get_event_loop()

        self.logger = logging.getLogger(__name__)
        self.root = Tk()

        self.root.title("BTTS")
        
        self.root.geometry("500x600")
        
        self.testLabel = Label(self.root, text="testLabel")
        self.testLabel.grid(row=2,column=3)
        self.testLabel.place(height=400,width=400)

        # Creates Login Buttom to open Twitch login page 
        self.loginBtn = Button(self.root, text="Login", command=self.loginOpen)
        self.loginBtn.grid(row=1,column=2, padx=10, pady=10)

        self.ttsBtn = Button(self.root, text="Start TTS", command=self.startTTS)
        self.ttsBtn.grid(row=2,column=2, padx=10,pady=10)
        if checkData() == None:
            self.ttsBtn["state"] = "disabled"
        else:
            self.ttsBtn["state"] = "normal"

        self.stopttsBtn = Button(self.root, text="Stop TTS", command=self.stopTTS, state="disabled") 
        self.stopttsBtn.grid(row=2, column=3, padx=10,pady=10)

    def loginOpen(self):
        try:
            self.login = Login()
            self.login.open()
            self.isOpened = True
            while self.isOpened:
                self.isOpened = self.login.get_isOpened()
                self.loginBtn.state = "DISABLED"
                self.ttsBtn["state"] = "normal"
                print("Login CloSED")
        except Exception as e:
            self.logger.exception(e)

    def startTTS(self):
    
        try:
            self.stopttsBtn["state"] = "normal"
            self.tts = TTV_Websocket()
            self.tts.Start()
        except Exception as e:
            self.logger.exception(e)

    def stopTTS(self):
        self.tts.Stop()

if __name__ == "__main__":
    ui = MainUI()

    ui.root.mainloop()
