
# Assignment 6A: Binary Search Tree
# Level Order Traversal, Height and Leaf Nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # Insert Node
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Level Order Traversal
    def level_order(self, root):
        if root is None:
            print("Tree is Empty!")
            return

        queue = [root]

        print("Level Order Traversal:")

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

    # Find Height
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
    print("\n===== BINARY SEARCH TREE =====")
    print("1. Insert Node")
    print("2. Display Original BST Level Wise")
    print("3. Display New (Mirror) Tree Level Wise")
    print("4. Find Height")
    print("5. Print Leaf Nodes")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter value: "))
        bst.root = bst.insert(bst.root, data)
        print("Node inserted successfully!")

    elif choice == '2':
        bst.level_order(bst.root)

    elif choice == '3':
        new_root = bst.mirror_tree(bst.root)
        print("New Mirror Tree:")
        bst.level_order(new_root)

    elif choice == '4':
        print("Height of BST:", bst.height(bst.root))

    elif choice == '5':
        if bst.root is None:
            print("Tree is Empty!")
        else:
            print("Leaf Nodes:")
            bst.leaf_nodes(bst.root)
            print()

    elif choice == '6':
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
