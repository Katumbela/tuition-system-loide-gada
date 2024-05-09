import flet as ft


def Store_Page(page):
    page.views.clear()
    return page.views.append(
        ft.View(
            "/store",
            [
                ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
            ],
        )
    )
