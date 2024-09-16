import flet as ft
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None: 
    page.tittle = "Numerical System Translator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False


    #Creating the menu bar

    menubar = ft.MenuBar(
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Sistema"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Binario"),
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Octal"),
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Decimal"),
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Hexadecimal"),

                    )

                ]
            ),
        ]
    )

    #Creating the calculate button

    calculateButton= ft.CupertinoButton(
            content=ft.Text("Calcular", color=ft.colors.WHITE),
            bgcolor=ft.colors.PURPLE_300,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(15),
            opacity_on_click=0.5,
    )

    #Defining the things that will be inside the window

    menu1 = menubar
    number_1: ft.TextField = ft.TextField(text_align= ft.TextAlign.LEFT , width=200)
    menu2= menubar
    number_2: ft.TextField = ft.TextField(text_align= ft.TextAlign.LEFT , width=200)

    



    page.add(
        ft.Row(
            controls=[
            ft.Column(
                [
                    menu1,
                    number_1,
                    menu2,
                    number_2,
                    calculateButton,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )

 
ft.app(main)