import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.current_contact = None

    def add_contact(self, name, phone, email, address):
        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contact_list = ""
        for contact in self.contacts:
            contact_list += f"{contact['Name']}: {contact['Phone']}\n"
        return contact_list

    def search_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]:
                return contact
        return None

    def update_contact(self, name, phone, email, address):
        if self.current_contact is not None:
            self.current_contact["Name"] = name
            self.current_contact["Phone"] = phone
            self.current_contact["Email"] = email
            self.current_contact["Address"] = address
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.current_contact = None
        else:
            messagebox.showerror("Error", "No contact selected for update.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact["Name"] == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                return
        messagebox.showerror("Error", "Contact not found.")

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contact_book = ContactBook()

        # UI Elements
        self.label = tk.Label(master, text="Contact Book", font=("Helvetica", 16))
        self.label.grid(row=0, column=1, pady=10)

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="W")

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")

        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5, sticky="W")

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")

        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5, sticky="W")

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=4, column=0, padx=10, pady=5, sticky="E")

        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=4, column=1, padx=10, pady=5, sticky="W")

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.grid(row=7, column=0, padx=10, pady=5, sticky="E")

        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=7, column=1, padx=10, pady=5, sticky="W")

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=10, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contact_book.add_contact(name, phone, email, address)
        else:
            messagebox.showerror("Error", "Name and phone are required.")

    def view_contacts(self):
        contact_list = self.contact_book.view_contacts()
        if contact_list:
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

    def search_contact(self):
        search_term = self.search_entry.get()
        if search_term:
            contact = self.contact_book.search_contact(search_term)
            if contact:
                messagebox.showinfo("Contact Found", f"{contact['Name']}: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
                self.contact_book.current_contact = contact
            else:
                messagebox.showinfo("Contact Not Found", "No contact found with the given search term.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        self.contact_book.update_contact(name, phone, email, address)

    def delete_contact(self):
        name = self.name_entry.get()
        self.contact_book.delete_contact(name)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
