import Binario

class Decimal:
    def __init__(self, valor):
        self.valor = valor

    def DecToBin(self):
            num = int(self.valor)
            binario = ""
            while num > 0:
                binario = str(num % 2) + binario
                num = num // 2
            bin = Binario.Binario(binario)
            return bin.valor