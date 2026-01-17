import flet as ft
from shortcuts.helper import THEME_COLOR
import asyncio

class LoginPage(ft.View):
    def __init__(self,page):
        super().__init__()

        self.username = ft.TextField(
            hint_text="Username",
            border_color=THEME_COLOR,
            border_radius=20,
            bgcolor="white",
            color=THEME_COLOR,
            cursor_color=THEME_COLOR
        )

        self.password = ft.TextField(
            hint_text="Password",
            border_color=THEME_COLOR,
            border_radius=20,
            can_reveal_password=True,
            password=True,
            bgcolor="white",
            color=THEME_COLOR,
            cursor_color=THEME_COLOR
        )

        self.button = ft.Button(
            content="Login",
            bgcolor=THEME_COLOR,
            color="white",
            width=500,
            on_click= lambda: asyncio.create_task(
                 self.LoginMethod()
            )
        )

        self.box = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Login"),
                    self.username,
                    self.password,
                    self.button,
                    ft.Text("Forgot Password?") 
                ],
                horizontal_alignment="center"
            ),
            padding=20,
            gradient=ft.LinearGradient(
                colors=[THEME_COLOR,"yellow"],
                 begin = ft. Alignment.CENTER_LEFT,
                 end  =  ft.Alignment.CENTER_RIGHT,
                 rotation=2.12
                
            ),
            width=300
        )

        self.controls = [
             self.box 
        ]
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        self.bgcolor = ft.Colors.BLACK
        self.padding = 20
        
    
    def build(self):
        return self.controls
    
    async def LoginMethod(self):
        if self.username.value == "" or self.password.value == "":
            print("Kindly Fill Required Details")
            self.page.show_dialog(
                ft.SnackBar(
                    content=ft.Text("Fill IT")
                )
            )
        
        elif self.username.value == "admin" or self.password.value == "1234":
            asyncio.create_task(
                self.page.push_route("/dashboard")
            )

            await ft.SharedPreferences().set("is_authenticated","True")
            # test = await ft.SharedPreferences().get("is_authenticated")
            # print(test)
        
        else:
            self.page.show_dialog(
                ft.SnackBar(
                    content=ft.Text("Kindly Fill Correct Details")
                )
            )
        

