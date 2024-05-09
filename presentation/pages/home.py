import flet as ft
from presentation.components.home_buttons import Columns_itens


def Home_Page(page):
    page.title = "Sistema De gestão de Propinas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    return page.views.append(
        ft.View(
            "/",
            [
                ft.ElevatedButton(
                    "Sobre o Sistema", on_click=lambda _: page.go("/store")
                ),
                ft.Container(
                    content=Columns_itens(page), margin=ft.margin.only(top=200)
                ),
            ],
        )
    )
