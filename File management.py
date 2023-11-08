 

#File Management Functions

import os

#Function to create file
def create_file(file_name):
    try:
        file = open(file_name, 'w')
        print(f"\nFile '{file_name}' created successfully.")
        file.close()
    except:
        print(f"\nError creating the file.")

#Function to read file
def read_file(file_name):
    if os.path.exists(file_name):
        file = open(file_name, 'r')
        content = file.read()
        print(f"\nContents of '{file_name}':\n{content}")
        file.close()
    else:
        print(f"\nFile '{file_name}' not found.")

#Function to add add file and content into file
def append_file(file_name, content):
    try:
        file = open(file_name, 'a')
        file.write(content + '\n')
        print(f"\nContent appended to '{file_name}' successfully.")
        file.close()
    except:
        print(f"\nError appending to the file.")

#Function to delete file
def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"\nFile '{file_name}' deleted successfully.")
    else:
        print(f"\nFile '{file_name}' not found.")

# Main program
while True:
    print("File Management System:")
    print("1. Create a New File")
    print("2. Read File")
    print("3. Append to File")
    print("4. Delete File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file_name = input("Enter the file name: ")
        create_file(file_name)
    elif choice == "2":
        file_name = input("Enter the file name: ")
        read_file(file_name)
    elif choice == "3":
        file_name = input("Enter the file name: ")
        content = input("Enter the content to append: ")
        append_file(file_name, content)
    elif choice == "4":
        file_name = input("Enter the file name: ")
        delete_file(file_name)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Enter a valid option.")
  

