import time

class Mob:
    def __init__(self, x, y, hp, type, mana, damage):
        self.x = x
        self.y = y
        self.hp = hp
        self.type = type
        self.mana = mana
        self.damage = damage
        self.h_speed = 1
        self.v_speed = 1

    def update(self):
        if self.y == 0 and 10 <= self.x < 60:
            self.x = self.x + self.h_speed
        elif 0 <= self.y < 50 and self.x == 60:
            self.y = self.y + self.v_speed
        elif self.y == 50 and 10 < self.x <= 60:
            self.x = self.x - self.h_speed
        elif self.x == 10 and 0 < self.y <= 50:
            self.y = self.y - self.v_speed



mob_1 = Mob(10, 0, 200, "boss", 100, 50)

run = True
while run == True:
    mob_1.update()
    print(mob_1.x, mob_1.y)
    time.sleep(0.1)