class Order:
    def __init__(self, user, cart):
        self.user = user
        self.total = cart.total()

    def save(self):
        with open("storage/db.txt", "a") as f:
            f.write(f"{self.user} | {self.total}\n")