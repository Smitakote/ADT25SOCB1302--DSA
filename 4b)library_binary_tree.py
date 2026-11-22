
# Assignment 4B: Library Catalog Navigation
# Binary Search Tree Implementation

class Node:
    def __init__(self, book_id):
        self.data = book_id
        self.left = None
        self.right = None


class BinarySearchTree:

    def insert(self, root, book_id):
        if root is None:
            return Node(book_id)

        if book_id < root.data:
            root.left = self.insert(root.left, book_id)

        elif book_id > root.data:
            root.right = self.insert(root.right, book_id)

        return root

    def search(self, root, book_id):
        if root is None:
            return False

        if root.data == book_id:
            return True

        if book_id < root.data:
            return self.search(root.left, book_id)

        return self.search(root.right, book_id)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Main Program
bst = BinarySearchTree()
root = None

while True:
    print("\n===== LIBRARY CATALOG =====")
    print("1. Insert Book ID")
    print("2. Search Book ID")
    print("3. Display Book IDs")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        book_id = int(input("Enter Book ID: "))
        root = bst.insert(root, book_id)
        print("Book ID inserted successfully!")

    elif choice == '2':
        book_id = int(input("Enter Book ID to search: "))

        if bst.search(root, book_id):
            print("Book ID found!")
        else:
            print("Book ID not found!")

    elif choice == '3':
        if root is None:
            print("Library catalog is empty!")
        else:
            print("Book IDs in sorted order:")
            bst.inorder(root)
            print()

    elif choice == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
