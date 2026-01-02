
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from menu import Menu
from monster_ai import MonsterAI
import saves, time, sys

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()
        self.accept("escape", sys.exit)
        self.menu = Menu(self.start_game)

    def start_game(self, ai_level):
        self.menu.frame.destroy()
        self.night_length = 600
        self.flashlight_power = 300
        self.start_time = time.time()
        self.monster_ai = MonsterAI(ai_level)
        self.player = self.camera
        self.player.setPos(0,0,2)
        self.monster = loader.loadModel("models/panda")
        self.monster.reparentTo(render)
        self.monster.setScale(0.5)
        self.monster.setPos(20,20,0)
        self.taskMgr.add(self.update, "update")

    def update(self, task):
        dt = globalClock.getDt()
        elapsed = time.time() - self.start_time
        if elapsed > self.night_length:
            print("YOU SURVIVED THE NIGHT")
            sys.exit()
        self.monster_ai.update(self.monster, self.player, dt)
        if (self.monster.getPos() - self.player.getPos()).length() < 2:
            print("THE MONSTER GOT YOU")
            sys.exit()
        return task.cont

Game().run()
