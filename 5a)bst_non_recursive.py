
# Assignment 5A: Binary Search Tree
# Inorder and Preorder Non-Recursive Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left

            elif data > temp.data:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right
            else:
                print("Duplicate value not allowed!")
                return

    # Non-Recursive Inorder Traversal
    def inorder(self):
        stack = []
        temp = self.root

        print("Inorder Traversal:")

        while temp is not None or stack:
            while temp is not None:
                stack.append(temp)
                temp = temp.left

            temp = stack.pop()
            print(temp.data, end=" ")
            temp = temp.right

        print()

    # Non-Recursive Preorder Traversal
    def preorder(self):
        if self.root is None:
            print("Tree is Empty!")
            return

        stack = [self.root]

        print("Preorder Traversal:")

        while stack:
            temp = stack.pop()
            print(temp.data, end=" ")

            if temp.right:
                stack.append(temp.right)

            if temp.left:
                stack.append(temp.left)

        print()


# Main Program
bst = BST()

while True:
    print("\n===== BINARY SEARCH TREE =====")
    print("1. Insert Node")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter value: "))
        bst.insert(data)
        print("Node inserted successfully!")

    elif choice == '2':
        bst.inorder()

    elif choice == '3':
        bst.preorder()

    elif choice == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
