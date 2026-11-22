
# Assignment 3: Singly Linked List
# College Library Book Management System

class Node:
    def __init__(self, book_id):
        self.data = book_id
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_beginning(self):
        book_id = input("Enter Book ID: ")

        new_node = Node(book_id)
        new_node.next = self.head
        self.head = new_node

        print("Book inserted at beginning successfully!")

    # Insert at End
    def insert_end(self):
        book_id = input("Enter Book ID: ")

        new_node = Node(book_id)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

        print("Book inserted at end successfully!")

    # Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            deleted = self.head.data
            self.head = self.head.next
            print("Deleted Book ID:", deleted)

    # Display Linked List
    def display(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            temp = self.head

            print("\nBook IDs in Library:")
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")


# Main Program
ll = LinkedList()

while True:
    print("\n===== LIBRARY BOOK MANAGEMENT =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        ll.insert_beginning()

    elif choice == '2':
        ll.insert_end()

    elif choice == '3':
        ll.delete_beginning()

    elif choice == '4':
        ll.display()

    elif choice == '5':
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
