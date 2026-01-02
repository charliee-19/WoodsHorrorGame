
from direct.gui.DirectGui import *

class Menu:
    def __init__(self, start_callback):
        self.frame = DirectFrame(frameColor=(0,0,0,1), frameSize=(-1,1,-1,1))
        DirectLabel(text="WOODS HORROR", scale=0.1, pos=(0,0,0.7), parent=self.frame)
        self.ai_slider = DirectSlider(range=(1,5), value=1, scale=0.4,
                                       pos=(0,0,0), parent=self.frame)
        DirectLabel(text="AI LEVEL", pos=(0,0,0.15), scale=0.05, parent=self.frame)
        DirectButton(text="START NIGHT", scale=0.1, pos=(0,0,-0.5),
                     command=lambda: start_callback(int(self.ai_slider['value'])))
