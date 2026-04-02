# Simple Data Saver

def add_data():
    name = input("Enter name: ")
    
    with open("data.txt", "a") as file:
        file.write(name + "\n")
    
    print("Saved successfully!")

def view_data():
    print("\nSaved Names:")
    with open("data.txt", "r") as file:
        print(file.read())

while True:
    print("\n1. Add Data")
    print("2. View Data")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        add_data()
    elif choice == "2":
        view_data()
    elif choice == "3":
        break
    else:
        print("Invalid choice")