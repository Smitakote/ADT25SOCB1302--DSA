
# Assignment 8B: Social Network Connectivity
# BFS using Adjacency List

from collections import deque

class SocialNetwork:
    def __init__(self):
        self.network = {}

    # Add User
    def add_user(self, user):
        if user not in self.network:
            self.network[user] = []

    # Add Friendship
    def add_friendship(self, user1, user2):
        self.add_user(user1)
        self.add_user(user2)

        self.network[user1].append(user2)
        self.network[user2].append(user1)

    # Display Network
    def display(self):
        print("\nSocial Network:")
        for user in self.network:
            print(user, "->", self.network[user])

    # BFS Level Wise
    def bfs(self, start):
        if start not in self.network:
            print("User not found!")
            return

        visited = set()
        queue = deque([start])
        visited.add(start)

        level = 0

        print("\nUsers Level Wise:")

        while queue:
            size = len(queue)

            print("Level", level, ":", end=" ")

            for i in range(size):
                user = queue.popleft()
                print(user, end=" ")

                for friend in self.network[user]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)

            print()
            level += 1


# Main Program
social = SocialNetwork()

n = int(input("Enter number of users: "))

print("Enter user names:")
for i in range(n):
    user = input()
    social.add_user(user)

e = int(input("Enter number of friendships: "))

for i in range(e):
    user1, user2 = input(
        "Enter friendship (user1 user2): "
    ).split()

    social.add_friendship(user1, user2)

social.display()

start = input("Enter starting user: ")

social.bfs(start)
