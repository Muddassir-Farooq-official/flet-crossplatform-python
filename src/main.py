import flet as ft
from pages.login import LoginPage
from pages.dashboard import DashboardPage
import asyncio

async def before(page:ft.Page):
    pass

async def main(page:ft.Page):
    page.window.always_on_top = True

    async def route_change():
        page.views.clear()

        if page.route == "/":
            view = LoginPage(page=page)
            page.views.append(view)
        
        elif page.route == "/dashboard":
            view = DashboardPage(page=page)
            page.views.append(view)

        


        page.update()

    page.on_route_change = route_change


    await route_change()


ft.run(main,before_main=before)