import flet as ft
from shortcuts.helper import THEME_COLOR
import datetime

class LoginPage(ft.View):
    def __init__(self,page):
        super().__init__()

        self.today = datetime.datetime.now()

        self.text = ft.TextField()

        self.data = ft.DatePicker(
              first_date=datetime.datetime(year=self.today.year - 1, month=1, day=1),
              last_date=datetime.datetime(year=self.today.year + 1, month=self.today.month, day=20),
              on_change=self.handle_change
              
        )
        
        self.controls = [
             self.text,
             ft.CupertinoButton(
                 content=ft.Text("Select Date",color="white"),
                 bgcolor=THEME_COLOR,
                 on_click=lambda e: page.show_dialog(self.data),
             ) 
        ]
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        self.bgcolor = ft.Colors.WHITE
        self.padding = 20
        
    
    def build(self):
        return self.controls
        
    def handle_change(self,e: ft.Event[ft.DatePicker]):
        print(e.control.value.strftime('%m/%d/%Y'))
        self.text.value = str(e.control.value.strftime('%m/%d/%Y'))
        self.text.update()
    
