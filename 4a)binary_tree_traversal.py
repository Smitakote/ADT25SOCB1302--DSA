
# Assignment 4A: Binary Tree Traversal
# Inorder, Preorder and Postorder

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# Creating Binary Tree
tree = BinaryTree()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Display Traversals
print("Inorder Traversal:")
tree.inorder(root)

print("\nPreorder Traversal:")
tree.preorder(root)

print("\nPostorder Traversal:")
tree.postorder(root)

print()
