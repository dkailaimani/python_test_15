# User Interface (UI):
# Create a user-friendly command-line interface (CLI) 
# for the Contact Management System.
# Display a welcoming message and provide a menu 
# with the following options:
#  <div class="oc-markdown-custom-container
#  oc-markdown-activatable" contenteditable="false" data-value="```
# Welcome to the Contact Management System! Menu:
# Add a new contact
# Edit an existing contact
# Delete a contact
# Search for a contact
# Display all contacts
# Export contacts to a text file
# Import contacts from a text file
# Quit

# Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier as the outer dictionary key.
# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).
# Menu Actions:

# Implement the following actions in response to menu selections:
# Adding a new contact with all relevant details.
# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact by searching for their unique identifier.
# Searching for a contact by their unique identifier and displaying their details.
# Displaying a list of all contacts with their unique identifiers.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system.

import os

def displayMenu():
    print("Welcome to the Contact Management System!\nMenu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def insertContact(contacts):
    contactId = input("ENTER CONTACT ID: ")
    if contactId in contacts:
        print("ERROR: ID ALREADY EXISTS!")
        return
    name = input("NAME: ")
    phone = input("PHONE NUMBER: ")
    email = input("EMAIL ADDRESS: ")
    extraInfo = input("INFO: ")
    contacts[contactId] = {"Name": name, "Phone": phone, "Email": email, "Additional Info": extraInfo}
    print("CONTACT INSERTED!")

def editContacts(contacts):
    contactId = input("ENTER ID TO EDIT: ")
    if contactId not in contacts:
        print("ERROR: CONTACT NOT FOUND!")
        return
    print("ENTER CONTACT INFO:")
    name = input(f"Name ({contacts[contactId]['Name']}): ") or contacts[contactId]['Name']
    phone = input(f"Phone ({contacts[contactId]['Phone']}): ") or contacts[contactId]['Phone']
    email = input(f"Email ({contacts[contactId]['Email']}): ") or contacts[contactId]['Email']
    extraInfo = input(f"Additional Info 
    ({contacts[contactId]['Additional Info']}):
     ") or contacts[contactId]['Additional Info']
    contacts[contactId] = {"Name": name, "Phone": 
    phone, "Email": email, "Additional Info": extraInfo}
    print("CONTACT EDITED.")

def deleteContact(contacts):
    contactId = input("ENTER ID OF CONTACT TO DELETE: ")
    if contactId not in contacts:
        print("CONTACT NOT FOUND!")
        return
    del contacts[contactId]
    print("CONTACT DELETED!")

def searchForContact(contacts):
    contactId = input("ENTER ID TO SEARCH: ")
    if contactId not in contacts:
        print("cONTACT NOT FOUND!")
        return
    print("CONTACT INFO:")
    print(contacts[contactId])

def displayContacts(contacts):
    if not contacts:
        print("CONTACT LIST EMPTY!")
        return
    print("CONTACTS: ")
    for contactId, contactInfo in contacts.items():
        print(f"ID: {contactId}")
        print(contactInfo)
        print()

def exportContactToFile(contacts):
    fileName = input("ENTER FILE NAME TO EXPORT CONTACTS: ")
    try:
        with open(fileName, 'w') as file:
            for contactId, contactInfo in contacts.items():
                file.write(f"{contactId}: {contactInfo}\n")
        print("ALL CONTACTS EXPORTED!")
    except Exception as e:
        print(f"ERROR: {e}")

def importContact(contacts):
    fileName = input("ENTER NAME OF FILE TO IMPORT CONTACT: ")
    try:
        with open(fileName, 'r') as file:
            for line in file:
                contactId, contactInfo = line.strip().split(": ", 1)
                contacts[contactId] = contactInfo
        print("ALL CONTACTS IMPORTED!")
    except FileNotFoundError:
        print("FILE DOESN'T EXIST!")
    except Exception as e:
        print(f"ERROR: {e}")

contacts = {}
while True:
    displayMenu()
    choice = input("CHOOSE FROM MENU: ")
    if choice == '1':
        insertContact(contacts)
    elif choice == '2':
        editContacts(contacts)
    elif choice == '3':
        deleteContact(contacts)
    elif choice == '4':
        searchForContact(contacts)
    elif choice == '5':
        displayContacts(contacts)
    elif choice == '6':
        exportContactToFile(contacts)
    elif choice == '7':
        importContact(contacts)
    elif choice == '8':
        print("APPLICATION TERMINATED!")
        break
    else:
        print("ERROR: ONLY ENTER NUMBER BETWEEN 1 AND 8!")
