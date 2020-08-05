import tkinter as tk
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from Components.auth.Login import Login


class MainUI(tk.Frame):

    def __init__(self):
        self.root = Tk()

        self.root.title("Test Title")
        
        self.root.geometry("500x600")
        
        self.testLabel = Label(self.root, text="testLabel")
        self.testLabel.grid(row=2,column=3)
        self.testLabel.place(height=400,width=400)

        # Creates Login Buttom to open Twitch login page 
        self.loginBtn = Button(self.root, text="Login", command=Login)
        self.loginBtn.grid(row=1,column=2, padx=10, pady=10)

if __name__ == "__main__":
    ui = MainUI()

    ui.root.mainloop()
