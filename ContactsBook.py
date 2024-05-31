import tkinter as tk
from tkinter import Frame

class ContactsBook:
    def __init__(self):
        self.createMainWindow()

    def createMainWindow(self):
        # utworzenie okna
        self.rootMain = tk.Tk()
        self.rootMain.title("Contacts App")
        self.rootMain.geometry("360x800")

        # utworzenie strony głównej
        self.homePage = Frame(self.rootMain)
        self.homePage.pack()

        # utworzenie strony dodawania
        self.addContactPage = Frame(self.rootMain)
        self.addContactPage.pack()

        # utworzenie strony zarządzania kontaktem
        self.manageContactPage = Frame(self.rootMain)
        self.manageContactPage.pack()


        # Uruchomienie okna
        self.rootMain.mainloop()