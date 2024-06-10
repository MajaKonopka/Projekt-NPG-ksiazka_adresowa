import tkinter as tk
from tkinter import Frame
from tkinter import messagebox as tkMessageBox
from Contact import Contact
import json

class ContactsBook:
    def __init__(self):
        """
        Inicjalizuje instancję klasy ContactsBook, odczytuje kontakty z pliku i tworzy główne okno aplikacji.
        """
        print(self.readFromFile())
        self.contactsList = self.readFromFile()
        self.createMainWindow()

    def createMainWindow(self):
        """
        Tworzy i konfiguruje główne okno oraz strony interfejsu graficznego (GUI).
        """
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

        # utworzenie miejsca na liste kontaktów
        self.contactsListbox = tk.Listbox(self.homePage)
        self.contactsListbox.pack(padx=40, pady=40)
        self.fillContactsListbox()

        # utworzenie search bara
        search_frame = tk.Frame(self.homePage)
        search_frame.pack(pady=10)
        search_label = tk.Label(search_frame, text="Search:")
        search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.searchContacts)

        # dodanie click listenera
        self.contactsListbox.bind("<<ListboxSelect>>", self.handleContactSelection)

        add_button = tk.Button(self.homePage, text="Add Contact", command=self.addContact)
        add_button.pack(pady=10)

        # Uruchomienie okna
        self.rootMain.mainloop()

    def addContact(self):
        """
        Dodaje nowy kontakt do listy kontaktów i aktualizuje interfejs użytkownika.
        """
        def submit():
            try:
                # Pobieranie danych z inputów
                name = entry1.get()
                surname = entry2.get()
                phoneNumber = int(entry3.get())

                self.contactsList.append(Contact(name, surname, phoneNumber))
                try:
                    self.saveToFile()
                except:
                    print("Error in saving file")
                print("Contact added successfully.")

                toTheHomePage()
            except:
                tkMessageBox.showwarning("Warning", "Incorrect information")

        def toTheHomePage():
            # Powrót do strony głównej
            self.fillContactsListbox()
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

    # Zapełnienie listy kontaktów

    def fillContactsListbox(self, search_query=""):
        # odświeżenie wyświetlanej listy
        self.contactsListbox.delete(0, tk.END)
        for contact in self.contactsList:
            if search_query.lower() in (contact.name + " " + contact.surname).lower():
                self.contactsListbox.insert(tk.END, f"{contact.name} {contact.surname}")

    def searchContacts(self, event):
        """
        Wyszukuje kontakty na podstawie wprowadzonego tekstu w pasku wyszukiwania.

        Parametry:
        event: Wydarzenie związane z naciśnięciem klawisza.
        """
        search_query = self.search_entry.get()
        self.fillContactsListbox(search_query)
        
    def handleContactSelection(self, event):
        """
        Obsługuje wybór kontaktu z listy kontaktów.

        Parametry:
        event: Wydarzenie związane z wyborem kontaktu.
        """
        selected_index = self.contactsListbox.curselection()
        if selected_index:
            selectedContact = self.contactsList[selected_index[0]]
            self.manageContact(selectedContact)
            print(f"Selected Contact: {selectedContact.name} {selectedContact.uuid}")

    def manageContact(self, contactData):
        def submit():
            try:
                # Pobieranie danych z inputów
                name = entry1.get()
                surname = entry2.get()
                phoneNumber = int(entry3.get())

                for contact in self.contactsList:
                    if contact.uuid == contactData.uuid:
                        contact.name = name
                        contact.surname = surname
                        contact.phoneNumber = phoneNumber
                try:
                    self.saveToFile()
                except:
                    print("Error in saving file")
                print("Contact added successfully.")

                toTheHomePage()
            except:
                tkMessageBox.showwarning("Warning", "Incorrect information")

        def toTheHomePage():
            # Powrót do strony głównej
            self.fillContactsListbox()
            self.homePage.pack()
            self.manageContactPage.pack_forget()

        def deleteContact():
            for contact in self.contactsList:
                if contact.uuid == contactData.uuid:
                    self.contactsList.remove(contact)
                    try:
                        self.saveToFile()
                    except:
                        print("Error in saving file")
                    print("Contact added successfully.")
            toTheHomePage()

        # Chowanie poprzedniej strony
        self.homePage.pack_forget()
        self.manageContactPage.pack()

        # Utworzenie inputów
        label1 = tk.Label(self.manageContactPage, text="Name:")
        label1.grid(row=0, column=0, padx=5, pady=5)
        entry1 = tk.Entry(self.manageContactPage)
        entry1.insert(0, contactData.name)
        entry1.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.manageContactPage, text="Surname:")
        label2.grid(row=1, column=0, padx=5, pady=5)
        entry2 = tk.Entry(self.manageContactPage)
        entry2.insert(0, contactData.surname)
        entry2.grid(row=1, column=1, padx=5, pady=5)

        label3 = tk.Label(self.manageContactPage, text="Phone Number:")
        label3.grid(row=2, column=0, padx=5, pady=5)
        entry3 = tk.Entry(self.manageContactPage)
        entry3.insert(0, contactData.phoneNumber)
        entry3.grid(row=2, column=1, padx=5, pady=5)

        # Przyciski
        submit_button = tk.Button(self.manageContactPage, text="Save changes", command=submit)
        submit_button.grid(row=3, column=0, padx=5, pady=5)

        clear_button = tk.Button(self.manageContactPage, text="Delete contact", command=deleteContact)
        clear_button.grid(row=3, column=1, padx=5, pady=5)

        clear_button = tk.Button(self.manageContactPage, text="Return", command=toTheHomePage)
        clear_button.grid(row=3, column=2, padx=5, pady=5)

    def printContacts(self):
        for n in self.contactsList:
            print(f"{n.name} \n{n.surname}")

    def readFromFile(self):
        """
        Odczytuje kontakty z pliku "contacts.json" i zwraca je jako listę obiektów Contact.

        Zwraca:
        list: Lista obiektów Contact.
        """
        contacts = []
        try:
            with open("contacts.json", "r") as file:
                    data = json.load(file)
                    for contact in data:
                        contacts.append(Contact(contact['name'], contact['surname'], contact['phoneNumber']))
        except:
            print("File is empty")
        return contacts
    def saveToFile(self):
        """
        Zapisuje bieżącą listę kontaktów do pliku "contacts.json".
        """
        with open("contacts.json", "w") as saveFile:
            json.dump(self.contactsList, saveFile, default=lambda x: x.__dict__)

