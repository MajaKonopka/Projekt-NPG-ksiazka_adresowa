import tkinter as tk
from tkinter import Frame
from tkinter import messagebox as tkMessageBox
from Contact import Contact

class ContactsBook:
    def __init__(self):
        self.contactsList = []
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

        # utworzenie miejsca na liste kontaktów
        self.contactsListbox = tk.Listbox(self.homePage)
        self.contactsListbox.pack(padx=40, pady=40)
        self.fillContactsListbox()

        # dodanie click listenera
        self.contactsListbox.bind("<<ListboxSelect>>", self.handleContactSelection)

        add_button = tk.Button(self.homePage, text="Add Contact", command=self.addContact)
        add_button.pack(pady=10)

        # Uruchomienie okna
        self.rootMain.mainloop()

    def addContact(self):

        def submit():
            try:
                # Pobieranie danych z inputów
                name = entry1.get()
                surname = entry2.get()
                phoneNumber = int(entry3.get())

                # Dodanie kontaktu do listy
                self.contactsList.append(Contact(name, surname, phoneNumber))
                print("Contact added successfully.")

                toTheHomePage()
            except:
                tkMessageBox.showwarning("Warning", "Incorrect information")

        def toTheHomePage():
            # Powrót do strony głównej
            self.homePage.pack()
            self.addContactPage.pack_forget()
            self.fillContactsListbox()
            self.printContacts()

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
    def fillContactsListbox(self):
        self.contactsListbox.delete(0, tk.END)
        for contact in self.contactsList:
                self.contactsListbox.insert(tk.END, f"{contact.name} {contact.surname}")

    def handleContactSelection(self, event):
        selected_index = self.contactsListbox.curselection()
        if selected_index:
            selectedContact = self.contactsList[selected_index[0]]
            self.manageContact(selectedContact)
            print(f"Selected Contact: {selectedContact.name} {selectedContact.uuid}")

    def manageContact(self, contactData):
        def toTheHomePage():
            # Powrót do strony głównej
            self.homePage.pack()
            self.manageContactPage.pack_forget()
            self.fillContactsListbox()
            self.printContacts()

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
        save_button = tk.Button(self.manageContactPage, text="Save changes", command="")
        save_button.grid(row=3, column=0, padx=5, pady=5)

        delete_button = tk.Button(self.manageContactPage, text="Delete contact", command="")
        delete_button.grid(row=3, column=1, padx=5, pady=5)

        return_button = tk.Button(self.manageContactPage, text="Return", command=toTheHomePage)
        return_button.grid(row=3, column=2, padx=5, pady=5)
    def printContacts(self):
        for n in self.contactsList:
            print(f"{n.name} \n{n.surname}")
