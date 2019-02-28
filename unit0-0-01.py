'''
Created on Feb 7, 2019

@author: s422530
'''
 # Created by: Sherwin Francis
 # Created on: 07022019
 # Created for: ICS3U
 # Daily Assignment Unit001
 # This program displays Hello World but with an menu to exit


from tkinter import *

class Application(Frame):
    def say_hi(self):
        print ("!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()