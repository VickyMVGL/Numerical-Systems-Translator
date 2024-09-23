import Binario

class hexadecimal:
    def __init__(self, valor):
        self.valor = valor
    
    def HexToBin(self):
        num = self.valor
        binario = ""
        numeros =[]
        for caracter in num:
            if caracter.lower() == "a":
                numeros.append(10)
            elif caracter.lower() == "b":
                numeros.append(11)
            elif caracter.lower() == "c":
                numeros.append(12)
            elif caracter.lower()== "d":
                numeros.append(13)
            elif caracter.lower() == "e":
                numeros.append(14)
            elif caracter.lower() == "f":
                numeros.append(15)
            else:
                numeros.append(int(caracter))       
        for numero in numeros:
            print (numero)
            if 8<= numero:
                binario = binario + "1"
                numero -= 8
            else:
                binario = binario + "0"
            if 4<= numero:
                binario = binario + "1"
                numero -= 4
            else:
                binario = binario + "0"
            
            if 2<= numero:
                binario = binario + "1"
                numero -= 2
            else:
                binario = binario + "0"
            
            if 1<= numero:
                binario = binario + "1"
                numero -= 1
            else:
                binario = binario + "0"
        bin= Binario(binario)
        return bin

