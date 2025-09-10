"""
Object Oriented Programming (OOP)
"""

# users = [
#     {"id": 0, "name": "Hero", "followers": [1, 2]},
#     {"id": 1, "name": "Dunn", "followers": [0]},
#     {"id": 2, "name": "Sue", "followers": []},
# ]


# def is_following(u1, u2):
#     return u1 in u2["followers"]


# print(is_following(0, users[1]))


class User:
    followers = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def follow(self, user):
        user.followers.append(self.id)

    def is_following(self, user):
        return self.id in user.followers


u1 = User(1, "hero")
print(u1.id)
print(u1.name)
print(u1.followers)

u2 = User(2, "big boss")
print(u2.id)
print(u2.name)
print(u2.followers)

u2.follow(u1)
print(u1.name, "has", len(u1.followers), "follower(s)")
print("Is u2 following u1?", u2.is_following(u1))
print("Is u1 following u2?", u1.is_following(u2))

u1.follow(u2)
print("Is u1 following u2?", u1.is_following(u2))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        # d=√((x2 – x1)² + (y2 – y1)²)

        return (((other.x - self.x) ** 2) + ((other.y - self.y) ** 2)) ** 0.5


p1 = Point(1, 2)
p2 = Point(3, 4)
d = p2 - p1
print(d)
