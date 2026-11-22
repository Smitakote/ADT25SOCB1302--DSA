
# Assignment 1: Stack Implementation
# Library Book Management System

stack = []

def return_book():
    book = input("Enter book name: ")
    stack.append(book)
    print(book, "returned successfully!")

def arrange_book():
    if len(stack) == 0:
        print("Stack is empty! No book to arrange.")
    else:
        book = stack.pop()
        print("Book arranged:", book)

def top_book():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Top book is:", stack[-1])

def display_stack():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("\nBooks in Stack (Top to Bottom):")
        for book in reversed(stack):
            print(book)

while True:
    print("\n===== LIBRARY BOOK MANAGEMENT =====")
    print("1. Return Book (Push)")
    print("2. Arrange Book (Pop)")
    print("3. Top Book (Peek)")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        return_book()

    elif choice == '2':
        arrange_book()

    elif choice == '3':
        top_book()

    elif choice == '4':
        display_stack()

    elif choice == '5':
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
