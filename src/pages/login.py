import flet as ft
from shortcuts.helper import THEME_COLOR
import asyncio

class LoginPage(ft.View):
    def __init__(self,page):
        super().__init__()

        self.data = [
            {
                "name":"ali",
                "class" : "23",
                "age": "18"
            },
            
            {
                "name":"ahmed",
                "class" : "20",
                "age": "21"
            },

             {
                "name":"raza",
                "class" : "12",
                "age": "19"
            }
        ]

        self.table = ft.Column(

            [

            ]
        )
        
        
        self.controls = [
             self.table 
        ]
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        self.bgcolor = ft.Colors.WHITE
        self.padding = 20

        
        
    
    def build(self):
        return self.controls
    
    async def load(self):
       for x in self.data:
            self.table.controls.append(

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(x["name"],size=23),
                            ft.Text(x["class"]),
                            ft.TextField(value=x["age"]),
                        ]
                    ),
                    padding=12,width=200,#height=100,
                    bgcolor=ft.Colors.random()
                )
            
        )
       self.page.update()

    def did_mount(self):
        asyncio.create_task(self.load())

    
        
    