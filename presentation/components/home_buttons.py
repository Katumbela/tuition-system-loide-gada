import flet as ft


def Columns_itens(page):
    def click_login():
        print("Clickable transparent with Ink clicked!")
        page.go("/login")

    return ft.Row(
        [
            ft.Container(
                content=ft.Image(src="https://img.icons8.com/dotty/80/user.png"),
                margin=20,
                on_click=lambda _: click_login(),
                padding=20,
                alignment=ft.alignment.center,
                width=170,
                bgcolor=ft.colors.BLUE_400,
                height=170,
                border_radius=10,
                ink=True,
            ),
            ft.Container(
                content=ft.Image(
                    src="https://img.icons8.com/ios/50/info--v1.png",
                ),
                margin=20,
                padding=20,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_400,
                width=170,
                height=170,
                border_radius=10,
                ink=True,
                on_click=lambda e: print("Clickable with Ink clicked!"),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
