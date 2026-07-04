from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size=(300,500)

class Calculator(BoxLayout): 
    def __init__(self,**kwargs):
        super().__init__(orientation='vertical',**kwargs)
        self.result=TextInput(
            font_size=45,
            size_hint_y=0.2,
            readonly=True,
            halign="right",
            multiline=False,
            background_color=[255/255, 255/255, 225/255, 1],
            foreground_color=[0/255, 0/255, 0/255, 1]
        )
        self.add_widget(self.result)

        Buttons=[
            ['C','+/-','%','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['0','Del','.','=']
        ]

        grid=GridLayout(cols=4, spacing=5 ,padding =10)
        for row in Buttons:
            for item in row:
                button=Button(
                    text=item,
                    font_size=32, 
                    background_color=self.set_button_color(item),
                    on_press=self.button_click
    
                )
                grid.add_widget(button)
        self.add_widget(grid)
    
    def set_button_color(self,color):
        if color in {'C','+/-','%'}:
            return [0.3,0.4,0.5,1]
        elif color in {'/','*','+','-','='}:
            return [0.8,0.6,0.7,1]
        return [0.1,0.1,0.2,1]
    
    def button_click(self,instance):
        text=instance.text #instance.text --> What button did the user press.

        if text=="C":
            self.result.text=""
        elif text=="=":
            self.calculate()
        elif text=="+/-":
            self.toggle_neg()
        elif text=="%":
            self.convert_percentage()
        elif text=='Del':
            self.delete()
        else:
            self.result.text+=text # self.result.text --> what is currently displayed on the calculator screen

    def calculate(self):
        try:
            self.result.text=str(eval(self.result.text))

        except Exception:
            self.result.text="ERROR!"
    
    def toggle_neg(self):
        if self.result.text:
            if self.result.text[0]== "-":
                self.result.text=self.result.text[1:]

            else:
                self.result.text='-'+self.result.text
    
    def convert_percentage(self):
        try:
            self.result.text=str(float(self.result.text)/100)
        except ValueError:
            self.result.text="ERROR!"

    def delete(self):
        self.result.text=self.result.text[:-1]

                
class CalculatorApp(App):
    def build(self):
        return Calculator()
 
if __name__=="__main__":
    CalculatorApp().run()


