from contact import Contact
class ContactList():
    def __init__(self):
        self.contacts = []
    def add(self,contact):
        self.contacts.append(contact)
    def display(self):
        print("Contact list:")
        for i in self.contacts:
            print(i)
