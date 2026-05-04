class Projectile:
    def __init__(self, x, y, speed, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction

    def move(self):
        # Update the position based on speed and direction
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

class ProjectileManager:
    def __init__(self):
        self.player_projectiles = []
        self.enemy_projectiles = []

    def add_player_projectile(self, projectile):
        self.player_projectiles.append(projectile)

    def add_enemy_projectile(self, projectile):
        self.enemy_projectiles.append(projectile)

    def update_projectiles(self):
        for projectile in self.player_projectiles:
            projectile.move()
        for projectile in self.enemy_projectiles:
            projectile.move()