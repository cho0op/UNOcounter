from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

class StartGame(Screen):
    player_name=ObjectProperty(None)
    players = ObjectProperty(None)
    def addPlayer(self):
        if self.player_name.text:
            self.players.text+=self.player_name.text+"\n"
            self.player_name.text=""



class WindowManager(ScreenManager):
    pass

class Counter(Screen):
    pass

kv=Builder.load_file("unocounter.kv")

class UnoCounter(App):
    def build(self):
        return kv


if __name__=="__main__":
    UnoCounter().run()