from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor =(1,1,1,1)
Window.size = (300, 400)
class Ui(Widget):
    def __init__(self, **kwargs):
        super(Ui,self).__init__(**kwargs)
        self.A= ''
        self.B=''
        self.intance =''
    def addNum(self,string):
        self.ids.num.text+=string
    def status(self,intan):
        self.intance =intan
        self.A = self.ids.num.text
        self.ids.solve.text = self.ids.num.text+self.intance
        self.ids.num.text=''

    def delStr(self):
        self.A =self.A[:-1]
        self.ids.num.text = self.A
    def solve(self):
        self.B = self.ids.num.text
        if self.intance =='+':
            result = float(self.A)+float(self.B)
        elif self.intance=='-':
            result =float(self.A)-float(self.B)
        elif self.intance=='x':
            result = float(self.A)*float(self.B)
        self.ids.solve.text += self.ids.num.text
        self.ids.num.text =str(result)
    def clear(self):
        self.ids.num.text=''
        self.ids.solve.text=''
        self.A=''
        self.B=''



class Te(App):
    def build(self):
        return Ui()

if  __name__  =='__main__':
    app =Te()
    app.run()

