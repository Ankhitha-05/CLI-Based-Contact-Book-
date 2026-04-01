contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("Contact added successfully\n")


def view_contacts():
    if not contacts:
        print("No contacts found \n")
        return
    
    print("\nAll Contacts:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    print()


def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False

    for c in contacts:
        if search_name in c["name"].lower():
            print(f"Found → Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
            found = True
    
    if not found:
        print("Contact not found ")
    print()


def delete_contact():
    name = input("Enter name to delete: ").lower()
    
    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            print("Contact deleted successfully 🗑️\n")
            return
    
    print("Contact not found \n")


def main():
    while True:
        print("==== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting... ")
            break
        else:
            print("Invalid choice \n")


if __name__ == "__main__":
    main()