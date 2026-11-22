
# Assignment 2: Queue Implementation Using Array
# Ticket Booking Counter

queue = []
MAX_SIZE = 5

def enqueue():
    if len(queue) == MAX_SIZE:
        print("Queue is Full! Cannot add customer.")
    else:
        customer = input("Enter customer name: ")
        queue.append(customer)
        print(customer, "added to the queue successfully!")

def dequeue():
    if len(queue) == 0:
        print("Queue is Empty! No customer to remove.")
    else:
        customer = queue.pop(0)
        print("Customer served:", customer)

def display():
    if len(queue) == 0:
        print("Queue is Empty!")
    else:
        print("\nCustomers in Queue:")
        for customer in queue:
            print(customer)

while True:
    print("\n===== TICKET BOOKING COUNTER =====")
    print("1. Enqueue (Add Customer)")
    print("2. Dequeue (Serve Customer)")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        enqueue()

    elif choice == '2':
        dequeue()

    elif choice == '3':
        display()

    elif choice == '4':
        print("Thank you for using Ticket Booking System!")
        break

    else:
        print("Invalid choice! Please try again.")
