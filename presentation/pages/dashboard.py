import flet as ft


def Dashboard_Page(page):
    page.views.clear()
    # Verifica se o usuário está autenticado
    if page.session.get("user") != "":
        user_data = page.session.get("user")
        username = user_data["name"]
        email = user_data["email"]
        page.views.append(
            ft.View(
                "/dashboard",
                [
                    ft.AppBar(
                        leading=ft.Image(
                            src=f"/icons/icons8-logout-64.png",
                            width=100,
                            height=100,
                        ),
                        leading_width=40,
                        center_title=True,
                        toolbar_height=120,
                        title=ft.Column(
                            spacing=0,
                            controls=[
                                ft.Image(
                                    src=f"/images/logo-1.png",
                                    width=300,
                                    height=70,
                                ),
                            ],
                        ),
                        bgcolor=ft.colors.WHITE,
                    ),
                    ft.Text(f"Welcome, {username}"),
                    ft.Text(f"Email: {email}"),
                ],
            )
        )
    else:
        page.views.append(
            ft.View(
                "/dashboard",
                [
                    ft.AppBar(
                        title=ft.Text("Dashboard"), bgcolor=ft.colors.SURFACE_VARIANT
                    ),
                    ft.Text("Please login to access the dashboard"),
                ],
            )
        )
    page.update()
