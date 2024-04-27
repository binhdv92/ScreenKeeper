import pyautogui
import time
import threading
from tkinter import Tk, Button, Label, StringVar
from datetime import datetime


class App:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.thread = None

        self.root.title("Screen Keeper")
        
        self.intro_var = StringVar()
        self.intro_var.set("Screen Keeper\n Powered by Van Binh Duong")
        self.intro_label = Label(root, textvariable=self.intro_var)
        self.intro_label.pack()

        self.status_var = StringVar()
        self.status_var.set("Stoped")

        #self.root.iconbitmap('FirstSolar_Icon.ico')
        self.status_label = Label(root, textvariable=self.status_var)
        self.status_label.pack()
        self.button = Button(root, text="Start", command=self.toggle)
        self.button.pack()

        self.clock_var = StringVar()
        self.clock_var.set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.clock_label= Label(root, textvariable=self.clock_var)
        self.clock_label.pack()

        self.toggle()

    def toggle(self):
        if self.running:
            self.running = False
            self.button.config(text="Start")
            self.status_var.set("Stopped")
        else:
            self.running = True
            self.button.config(text="Stop")
            self.status_var.set("Running")
            if self.thread is None or not self.thread.is_alive():
                self.thread = threading.Thread(target=self.keep_screen_active, daemon=True)
                self.thread.start()
                self.clock_thread = threading.Thread(target=self.update_clock, daemon=True)
                self.clock_thread.start()

    def keep_screen_active(self):
        while self.running:
            time.sleep(60)  # wait 60 seconds
            pyautogui.move(1, 0)
            time.sleep(1)
            pyautogui.move(-1, 0)

    def update_clock(self):
        while self.running:
            self.clock_var.set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(0.5)  # update every 1 second

root = Tk()
app = App(root)
root.mainloop()