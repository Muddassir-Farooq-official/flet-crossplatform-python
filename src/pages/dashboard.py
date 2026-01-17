import flet as ft
from shortcuts.helper import THEME_COLOR
import asyncio

class DashboardPage(ft.View):
    def __init__(self,page):
        super().__init__()

        
        self.controls = [
            ft.Text("Dashboard", color="White"),
            ft.IconButton(
                icon=ft.Icons.LOGOUT,
                icon_color="white",
                on_click=lambda: asyncio.create_task(self.clear_data())
            ) # This was the bracket causing the crash
        ]
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        self.bgcolor = ft.Colors.BLACK
        self.padding = 20
        self.appbar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click= lambda :   asyncio.create_task(
                self.page.push_route("/")
            )
            ),
            title=ft.Text("Dashboard")
        )

    async def clear_data(self):
        await ft.SharedPreferences.remove("is_authenticated")
        
    
    def build(self):
        return self.controls
