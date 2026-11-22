
# Assignment 10B: Parking Slot Allocation System
# Hash Table using Linear Probing
# Without Replacement

class ParkingSystem:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size

    # Hash Function
    def hash_function(self, vehicle):
        return vehicle % self.size

    # Park Vehicle
    def park_vehicle(self, vehicle):
        index = self.hash_function(vehicle)

        if self.slots[index] is None:
            self.slots[index] = vehicle
            print("Vehicle parked at slot:", index)
            return

        # Linear Probing
        for i in range(1, self.size):
            new_index = (index + i) % self.size

            if self.slots[new_index] is None:
                self.slots[new_index] = vehicle
                print("Slot occupied! Collision occurred.")
                print("Vehicle parked at slot:", new_index)
                return

        print("Parking is Full! No slot available.")

    # Search Vehicle
    def search_vehicle(self, vehicle):
        index = self.hash_function(vehicle)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.slots[new_index] is None:
                break

            if self.slots[new_index] == vehicle:
                print("Vehicle found at slot:", new_index)
                return

        print("Vehicle not found!")

    # Display Parking Slots
    def display(self):
        print("\n===== PARKING SLOT STATUS =====")

        for i in range(self.size):
            if self.slots[i] is None:
                print("Slot", i, ": Empty")
            else:
                print("Slot", i, ": Vehicle", self.slots[i])


# Main Program
size = int(input("Enter total parking slots: "))

parking = ParkingSystem(size)

while True:
    print("\n===== PARKING SLOT ALLOCATION =====")
    print("1. Park Vehicle")
    print("2. Search Vehicle")
    print("3. Display Parking Slots")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        vehicle = int(input("Enter vehicle number: "))
        parking.park_vehicle(vehicle)

    elif choice == '2':
        vehicle = int(input("Enter vehicle number to search: "))
        parking.search_vehicle(vehicle)

    elif choice == '3':
        parking.display()

    elif choice == '4':
        print("Thank you for using Parking System!")
        break

    else:
        print("Invalid choice! Please try again.")
