
# Assignment 5B: Student Admission Record Management
# Binary Search Tree using Roll Numbers

class Node:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.left = None
        self.right = None


class StudentBST:
    def __init__(self):
        self.root = None

    # Insert Student Record
    def insert(self, roll_no, name):
        new_node = Node(roll_no, name)

        if self.root is None:
            self.root = new_node
            print("Student record inserted!")
            return

        temp = self.root

        while True:
            if roll_no < temp.roll_no:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left

            elif roll_no > temp.roll_no:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right

            else:
                print("Roll number already exists!")
                return

        print("Student record inserted!")

    # Non-Recursive Inorder Traversal
    def inorder(self):
        stack = []
        temp = self.root

        if temp is None:
            print("No student records found!")
            return

        print("\nInorder Student Records:")

        while temp is not None or stack:
            while temp is not None:
                stack.append(temp)
                temp = temp.left

            temp = stack.pop()

            print("Roll No:", temp.roll_no,
                  "| Name:", temp.name)

            temp = temp.right

    # Non-Recursive Preorder Traversal
    def preorder(self):
        if self.root is None:
            print("No student records found!")
            return

        stack = [self.root]

        print("\nPreorder Student Records:")

        while stack:
            temp = stack.pop()

            print("Roll No:", temp.roll_no,
                  "| Name:", temp.name)

            if temp.right:
                stack.append(temp.right)

            if temp.left:
                stack.append(temp.left)


# Main Program
bst = StudentBST()

while True:
    print("\n===== STUDENT ADMISSION SYSTEM =====")
    print("1. Insert Student Record")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")

        bst.insert(roll_no, name)

    elif choice == '2':
        bst.inorder()

    elif choice == '3':
        bst.preorder()

    elif choice == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
