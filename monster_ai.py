
class MonsterAI:
    def __init__(self, level):
        self.level = level
        self.speed = 2 + level
        self.memory = []

    def learn(self, pos):
        self.memory.append(pos)
        if len(self.memory) > 30:
            self.memory.pop(0)

    def update(self, monster, player, dt):
        self.learn(player.getPos())
        if self.memory:
            target = self.memory[-1]
            direction = target - monster.getPos()
            direction.normalize()
            monster.setPos(monster.getPos() + direction * self.speed * dt)
