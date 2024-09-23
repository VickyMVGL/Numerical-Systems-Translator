import Binario

class Octal:
    def __init__(self, valor):
        self.valor = valor

    def OctalToBin(self):
        num = self.valor
        binario = ""
        numeros =[]
        while num > 0:
            numeros.append(num % 10)
            num = num // 10
        numeros.reverse()
        for numero in numeros:
            print (numero)
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
            
        bin = Binario(binario)
        return bin