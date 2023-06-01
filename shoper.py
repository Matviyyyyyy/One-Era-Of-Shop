from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView



class ShopScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    def toLoginScr(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'log_in'

class Registr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def toShopScr(self):
        if self.ids.intex1.text == "pon" and self.ids.intex2.text == "pon2":
            self.manager.transition.direction = 'left'
            self.manager.current = 'shop'
        elif self.ids.intex1.text != "pon" or self.ids.intex2.text != "pon2":
            self.ids.intex1.background_color = (1, 1, 1, 0)
            self.ids.intex2.background_color = (1, 1, 1, 0)
            self.ids.goshop.background_color = (1, 1, 1, 0)
            self.ids.goshop.opacity = 0
            leb = Label(text = "Неправильний логін або пароль!!!")
            self.ids.layout.add_widget(leb)
            



            


    






class RareApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Registr(name = 'log_in'))
        sm.add_widget(ShopScr(name = "shop"))
        return sm
if __name__  == '__main__':
    app = RareApp()
    app.run()
