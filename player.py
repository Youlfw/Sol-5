class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10
        self.inventory = []
        self.upgrades = []
        self.position = (0, 0)

    def move(self, x, y):
        self.position = (x, y)
        print(f"{self.name} moved to {self.position}")

    def shoot(self):
        print(f"{self.name} shoots dealing {self.damage} damage!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health is now {self.health}.")

    def upgrade(self, upgrade_type):
        self.upgrades.append(upgrade_type)
        print(f"{self.name} received upgrade: {upgrade_type}")

    def collect_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} collected an item: {item}")