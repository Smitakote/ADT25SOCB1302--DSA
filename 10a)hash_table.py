
# Assignment 10A: Hash Table
# Collision Handling using Linear Probing
# Without Replacement

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash Function
    def hash_function(self, key):
        return key % self.size

    # Insert Element
    def insert(self, key):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = key
            print("Element inserted successfully!")
            return

        # Linear Probing
        for i in range(1, self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                self.table[new_index] = key
                print("Collision occurred!")
                print("Element inserted at index:", new_index)
                return

        print("Hash Table is Full!")

    # Search Element
    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                break

            if self.table[new_index] == key:
                print("Element found at index:", new_index)
                return

        print("Element not found!")

    # Display Hash Table
    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(i, ":", self.table[i])


# Main Program
size = int(input("Enter hash table size: "))
ht = HashTable(size)

while True:
    print("\n===== HASH TABLE =====")
    print("1. Insert Element")
    print("2. Search Element")
    print("3. Display Hash Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter element: "))
        ht.insert(key)

    elif choice == '2':
        key = int(input("Enter element to search: "))
        ht.search(key)

    elif choice == '3':
        ht.display()

    elif choice == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
