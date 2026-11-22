
# Assignment 6B: Employee Database Analysis
# Binary Search Tree

class Node:
    def __init__(self, emp_id):
        self.data = emp_id
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # Insert Employee ID
    def insert(self, root, emp_id):
        if root is None:
            return Node(emp_id)

        if emp_id < root.data:
            root.left = self.insert(root.left, emp_id)

        elif emp_id > root.data:
            root.right = self.insert(root.right, emp_id)

        return root

    # Display Tree Level Wise
    def level_order(self, root):
        if root is None:
            print("Tree is Empty!")
            return

        queue = [root]

        while queue:
            size = len(queue)

            for i in range(size):
                temp = queue.pop(0)
                print(temp.data, end=" ")

                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

            print()

    # Create Mirror Tree
    def mirror_tree(self, root):
        if root is None:
            return None

        new_node = Node(root.data)

        new_node.left = self.mirror_tree(root.right)
        new_node.right = self.mirror_tree(root.left)

        return new_node

    # Find Height of Tree
    def height(self, root):
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)

    # Print Leaf Nodes
    def leaf_nodes(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            print(root.data, end=" ")
            return

        self.leaf_nodes(root.left)
        self.leaf_nodes(root.right)


# Main Program
bst = BST()

while True:
    print("\n===== EMPLOYEE DATABASE =====")
    print("1. Insert Employee ID")
    print("2. Display Original BST Level Wise")
    print("3. Display New Mirror Tree Level Wise")
    print("4. Find Height of Tree")
    print("5. Display Leaf Nodes")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        emp_id = int(input("Enter Employee ID: "))
        bst.root = bst.insert(bst.root, emp_id)
        print("Employee ID inserted successfully!")

    elif choice == '2':
        print("\nOriginal BST:")
        bst.level_order(bst.root)

    elif choice == '3':
        new_root = bst.mirror_tree(bst.root)
        print("\nNew Mirror Tree:")
        bst.level_order(new_root)

    elif choice == '4':
        print("Height of Tree:", bst.height(bst.root))

    elif choice == '5':
        if bst.root is None:
            print("Tree is Empty!")
        else:
            print("Leaf Employee IDs:")
            bst.leaf_nodes(bst.root)
            print()

    elif choice == '6':
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
