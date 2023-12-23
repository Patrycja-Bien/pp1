""""
22.	The Contact class contains the 'name', 'email' and 'telephone' fields enabling the description 
of a single contact on a smartphone. The Contact_List class allows you to store contacts (store 
objects describing contacts in an array) and perform the following operations:
a.	Adds a new contact
b.	Displays the contact list
Write a program consisting of 3 files (smartphone.py, contact.py, contact_list.py). 
In the mail program (smartphone.py) create an object representing a contact list and add the 
following people data:
John Brown     brown@onet.pl       555234000
Anna May   	am@o2.pl            232000199
George Small   smallg@google.pl    222999100
Paola Big      bigpaola@poczta.pl  100200300
Then, display the contact list available on the smartphone.
"""
from contact_list import ContactList
from contact import Contact

CList = ContactList()
contact1 = Contact("John Brown","brown@onet.pl",555234000)
contact2 = Contact("Anna May","am@o2.pl",232000199)
contact3 = Contact("George Small","smallg@google.pl",222999100)
contact4 = Contact("Paola Big","bigpaola@poczta.pl",100200300)

CList.add(contact1)
CList.add(contact2)
CList.add(contact3)
CList.add(contact4)

CList.display()