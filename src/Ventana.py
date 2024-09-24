import flet as ft
from flet_core.control_event import ControlEvent
#Importamos las clases que se crearon
import Binario
import Decimal
import Octal
import Hexadecimal


def main(page: ft.Page) -> None: 
    page.tittle = "Numerical System Translator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor="#2A314E"
    page.window_width = 1200
    page.window_height = 700
    page.window_resizable = False

    #Creando las funciones necesarias


    def calcular(e):
        sistema1=options1.value
        sistema2=options2.value

        if sistema1 == "Octal":
            traducir = Octal.Octal(number_1.value)
            tBin = Binario.Binario(traducir.OctalToBin())
        elif sistema1 == "Decimal":
            traducir = Decimal.Decimal(number_1.value)
            tBin = Binario.Binario(traducir.DecToBin())
        elif sistema1 == "Hexadecimal":
            traducir = Hexadecimal.Hexadecimal(number_1.value)
            tBin = Binario.Binario(traducir.HexToBin())
        elif sistema1 == "Binario":
            tBin = Binario.Binario(number_1.value)
        else: 
            print("Dios, espero no veas este mensaje, si ves este mensaje, algo salio mal")
        
        if sistema2 == "Octal":
            traducido = tBin.BinToOctal()
            number_2.value = str(traducido)
            page.update()
        elif sistema2 == "Decimal":
            traducido = tBin.BinToDec()
            number_2.value = str(traducido)
            page.update()
        elif sistema2 == "Hexadecimal":
            traducido = tBin.BinToHex()
            number_2.value = str(traducido)
            page.update()
        elif sistema2 == "Binario":
            traducido = tBin.valor
            number_2.value = str(traducido)
            page.update()

    #Creating the menu bar

    options1 = ft.Dropdown(
        options=[
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        width= 150,
        border_color= "#f7b176",
        value="Decimal",
        color= "#fefefe",
        bgcolor="#2A314E"
        )
    
    options2 = ft.Dropdown(
        options=[
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        width= 150,
        border_color= "#f7b176",
        value="Binario",
        color= "#fefefe",
        bgcolor="#2A314E",
        
        )

    
    #Creating the calculate button
    
    calculateButton= ft.FilledButton(
            text="Calcular",
            on_click=calcular,
            style=ft.ButtonStyle(
                bgcolor="#F7B176",
                color="#2A314E",
                
        ),
    )

    #Defining the things that will be inside the window
    def validar(e):

        sistema1=options1.value
        sistema2=options2.value

        valor = e.control.value
        caracteres =[]
        for caracter in valor:
            caracteres.append(caracter)

        #Validaciones del sistema binario

        if sistema1 == "Binario":
            for caracter in caracteres:
                if not caracter.isdigit():
                    number_1.error_text = "solo se permiten digitos del 0 al 1"
                elif int(caracter)<0 or int(caracter)>7:
                    number_1.error_text = "solo se permiten digitos del 0 al 1"
                else:
                    number_1.error_text = None
                page.update()
        #Validaciones del sistema Octal

        elif sistema1 == "Octal":
            for caracter in caracteres:
                if not caracter.isdigit():
                    number_1.error_text = "solo se permiten digitos del 0 al 7"
                elif int(caracter)<0 or int(caracter)>7:
                    number_1.error_text = "solo se permiten digitos del 0 al 7"
                else:
                    number_1.error_text = None
                page.update()

        #Validaciones del sistema Decimal
        elif sistema1 == "Decimal":
            for caracter in caracteres:
                if not caracter.isdigit():
                    number_1.error_text = "solo se permiten digitos del 0 al 9"
                elif int(caracter)<0 or int(caracter)>9:
                    number_1.error_text = "solo se permiten digitos del 0 al 9"
                else:
                    number_1.error_text = None
                page.update()

        #Validaciones del sistema hexadecimal
        elif sistema1 == "Hexadecimal":
            for caracter in caracteres:
                if not caracter.isdigit():
                    if caracter.upper() == "A":
                        number_1.error_text = None
                      
                    elif caracter.upper() == "B":
                        number_1.error_text = None
                        
                    elif caracter.upper() == "C":
                        number_1.error_text = None
                        
                    elif caracter.upper() == "D":
                        number_1.error_text = None
                       
                    elif caracter.upper() == "E":
                        number_1.error_text = None
                        
                    elif caracter.upper() == "F":
                        number_1.error_text = None
                        
                    else:
                        number_1.error_text = "solo se permiten digitos (0-9) y letras (A-F)"
                        
                elif int(caracter)<0 or int(caracter)>9:
                    number_1.error_text = "solo se permiten digitos (0-9) y letras (A-F)"
                    
                else:
                    number_1.error_text = None
                page.update()
            
    titulo = ft.Text(value="Traductor", color="#FEFEFE", size=60)
    subtitulo = ft.Text(value="de sistemas numericos", color="#F7B176", size=45, )
    menu1 = options1
    number_1: ft.TextField = ft.TextField(text_align= ft.TextAlign.LEFT , width=350,  label="Numero a Traducir", color="#fefefe", border_color="#F7B176")
    number_1.on_change = validar
    menu2= options2
    number_2: ft.TextField = ft.TextField(text_align= ft.TextAlign.LEFT , width=350, label="Numero Traducido", disabled=True, color="#fefefe", border_color="#F7B176")


    

    page.add(
        ft.Row(
            controls=[
            ft.Column(
                [
                    titulo,
                    subtitulo,
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