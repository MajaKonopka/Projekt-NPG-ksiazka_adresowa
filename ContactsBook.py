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

        add_button = tk.Button(self.homePage, text="Add Contact", command=self.addContact)
        add_button.pack(pady=10)

        # Uruchomienie okna
        self.rootMain.mainloop()

    def addContact(self):
        def submit():
            print("submitted")

        def toTheHomePage():
            # Powrót do strony głównej
            self.homePage.pack()
            self.addContactPage.pack_forget()

        # Chowanie poprzedniej strony
        self.homePage.pack_forget()
        self.addContactPage.pack()

        # Utworzenie inputów
        label1 = tk.Label(self.addContactPage, text="Name:")
        label1.grid(row=0, column=0, padx=5, pady=5)
        entry1 = tk.Entry(self.addContactPage)
        entry1.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.addContactPage, text="Surname:")
        label2.grid(row=1, column=0, padx=5, pady=5)
        entry2 = tk.Entry(self.addContactPage)
        entry2.grid(row=1, column=1, padx=5, pady=5)

        label3 = tk.Label(self.addContactPage, text="Phone Number:")
        label3.grid(row=2, column=0, padx=5, pady=5)
        entry3 = tk.Entry(self.addContactPage)
        entry3.grid(row=2, column=1, padx=5, pady=5)

        # Przyciski
        submit_button = tk.Button(self.addContactPage, text="AddContact", command=submit)
        submit_button.grid(row=3, column=0, padx=5, pady=5)

        clear_button = tk.Button(self.addContactPage, text="Return", command=toTheHomePage)
        clear_button.grid(row=3, column=1, padx=5, pady=5)