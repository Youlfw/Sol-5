# enemies.py

class Enemy:  
    def __init__(self, health, speed):  
        self.health = health  
        self.speed = speed  

    def take_damage(self, damage):  
        self.health -= damage  
        if self.health <= 0:  
            self.die()  

    def die(self):  
        print("Enemy has died")  

class BasicEnemy(Enemy):  
    def __init__(self):  
        super().__init__(health=100, speed=5)  
        
class FastEnemy(Enemy):  
    def __init__(self):  
        super().__init__(health=70, speed=10)  
        
class TankEnemy(Enemy):  
    def __init__(self):  
        super().__init__(health=150, speed=3)  

class EnemyManager:  
    def __init__(self):  
        self.enemies = []  

    def spawn_enemy(self, enemy_type):  
        if enemy_type == 'basic':  
            enemy = BasicEnemy()  
        elif enemy_type == 'fast':  
            enemy = FastEnemy()  
        elif enemy_type == 'tank':  
            enemy = TankEnemy()  
        else:  
            raise ValueError(f"Unknown enemy type: {enemy_type}")  
        self.enemies.append(enemy)  
        return enemy  

    def update_enemies(self):  
        for enemy in self.enemies:  
            # Logic for updating enemy state  
            pass  
