import flet as ft
from presentation.pages.store import Store_Page
from presentation.pages.home import Home_Page
from presentation.pages.login import Login_Page
from presentation.pages.dashboard import Dashboard_Page


def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        Home_Page(page)
        if page.route == "/store":
            Store_Page(page)

        elif page.route == "/login":
            Login_Page(page)

        elif page.route == "/dashboard":
            Dashboard_Page(page)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
