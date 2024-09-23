import Binario

class Decimal:
    def __init__(self, valor):
        self.valor = valor

    def DecToBin(self):
            num = self.valor
            binario = ""
            while num > 0:
                binario = str(num % 2) + binario
                num = num // 2
            bin = Binario(binario)
            return bin