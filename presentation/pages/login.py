from time import sleep
import flet as ft
import requests
import json


def Login_Page(page):
    page.title = "Entrar no sistema"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campos do formulário
    username_field = ft.TextField(
        label="Nome de Usuário",
    )

    password_field = ft.TextField(
        label="Senha",
        password=True,  # Para esconder o texto digitado
    )

    # Botão de envio do formulário
    login_button = ft.ElevatedButton(
        "Login",
        on_click=lambda _: submit_login(page, username_field, password_field),
    )

    # Botão para voltar para a página inicial
    home_button = ft.ElevatedButton(
        "Voltar para Home",
        on_click=lambda _: page.go("/"),
    )

    # Adicionando widgets à view
    page.views.append(
        ft.View(
            "/login",
            [
                home_button,
                username_field,
                password_field,
                login_button,
            ],
        )
    )


dlg = ft.AlertDialog(
    title=ft.Text("Login bem sucedido!."),
    on_dismiss=lambda e: print("Dialog dismissed!"),
)


def open_dlg(page):
    page.dialog = dlg
    dlg.open = True
    page.update()


dlg_error = ft.AlertDialog(
    title=ft.Text("Erro ao fazer login. Por favor, verifique suas credenciais."),
    on_dismiss=lambda e: print("Dialog dismissed!"),
)


def open_dlg_error(page):
    page.dialog = dlg_error
    dlg_error.open = True
    page.update()


def submit_login(page, username, password):
    # Endpoint de login
    login_url = "http://127.0.0.1:8000/api/login"

    # Dados do formulário
    data = {"email": username.value, "password": password.value}
    # print(data)

    response = requests.post(login_url, data=data)

    if response.status_code == 200:

        response_data = json.loads(response.text)
        token = response_data["token"]
        user_data = response_data["user"]

        # Armazena o token e os dados do usuário na sessão
        page.session.set("token", token)
        page.session.set("user", user_data)
        print(user_data)

        # Exibe uma mensagem de sucesso
        open_dlg(page)

        # Redireciona para a próxima página, se necessário
        sleep(3)
        page.go("/dashboard")
    else:
        # Se houver algum erro, exibe o diálogo de erro
        open_dlg_error(page)

        # Exibe detalhes do erro para fins de depuração
        print(response.text)
