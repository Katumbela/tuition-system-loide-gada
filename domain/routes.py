import flet as ft
from domain.routes import *
from presentation.pages import login


def route_change(page: ft.Page):
    page.views.clear()
    if page.route == "/":
        main_route(page)
    elif page.route == "/store":
        store_route(page)
    elif page.route == "/login":
        login.login_route(page)
    page.update()


def view_pop(page: ft.Page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)


def main_route(page: ft.Page):
    # page.views.clear()
    page.controls.append(
        ft.View(
            "/",
            [
                ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
            ],
        )
    )
    page.update()


def store_route(page: ft.Page):
    page.views.clear()
    page.views.append(
        ft.View(
            "/store",
            [
                ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
            ],
        )
    )
    page.update()
