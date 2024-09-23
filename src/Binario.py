class Binario:
    def __init__(self, valor):
        self.valor = valor
    
    def BinToDec(self):
        num = self.valor
        decimal = 0
        numeros =[]
        for caracter in num:
            numeros.append(int(caracter))
            print(numeros[:])
        numeros.reverse()
        print(numeros[:])
        cont= 0 
        while cont < len(numeros):
            print(int(numeros[cont]))
            decimal = decimal + (int(numeros[cont]) * (2 ** cont))
            cont +=1
        return decimal

    def BinToOctal(self):

        #Creamos una cadena para almacenar los digitos del numero binario
        num = self.valor
        octal= ""
        numeros =[]
        for caracter in num:
            numeros.append(int(caracter))
            print(numeros[:])

        #Revertimos la cadena para leer el numero de derecha a izquierda
        numeros.reverse()

        #Validacion para poder dividir los digitos en grupos de 3
        #En caso de que falten numeros se agrega un cero
        if len(numeros)%3 == 0 :
                mientras = ""
        else:
            numeros.append(0)
            if len(numeros)%3 == 0:
                    mientras = ""
            else:
                numeros.append(0)
                mientras = ""
        cont= 0 
        mientras =""
        while cont < len(numeros):
            for i in  range(3):
                #Se toma un valor provicional que formara los grupos de 3 digitos

                mientras =  str(numeros[cont]) + mientras
                cont +=1
            
            contMientras=[]
            for caracter in mientras:
                contMientras.append(int(caracter))
            
            a = contMientras[2]
            b = contMientras[1]
            c = contMientras[0]
            
            #se crea un valor temporal que va a ir sumando para agregarse al numero octal final
            temp = 0
            if a == 1:
                temp = temp + 1
            else: 
                temp= temp + 0
            if b == 1:
                temp = temp + 2
            else: 
                temp= temp + 0
            if c == 1:
                temp = temp + 4
            else: 
                temp= temp + 0
            print(temp)

            octal = str(temp) + octal
            mientras = ""
        
        #Logramos obtener el numero!!!!!
        return octal
    
    def BinToHex(self):
        #Creamos una cadena para almacenar los digitos del numero binario
        num = self.valor
        hex= ""
        numeros =[]
        for caracter in num:
            numeros.append(int(caracter))
            print(numeros[:])

        #Revertimos la cadena para leer el numero de derecha a izquierda
        numeros.reverse()

        #Validacion para poder dividir los digitos en grupos de 4
        #En caso de que falten numeros se agrega un cero
        if len(numeros)%4 == 0 :
                mientras = ""
        else:
            numeros.append(0)
            if len(numeros)%4 == 0:
                    mientras = ""
            else:
                numeros.append(0)
            if len(numeros)%4 == 0:
                    mientras = ""
            else:
                numeros.append(0)
                mientras = ""

        cont= 0 
        mientras =""
        while cont < len(numeros):
            for i in  range(4):
                #Se toma un valor provicional que formara los grupos de 3 digitos
                mientras =  str(numeros[cont]) + mientras
                cont +=1
            
            contMientras=[]
            for caracter in mientras:
                contMientras.append(int(caracter))
            
            a = contMientras[3]
            b = contMientras[2]
            c = contMientras[1]
            d = contMientras[0]
            
            #se crea un valor temporal que va a ir sumando para agregarse al numero octal final
            temp = 0
            if a == 1:
                temp = temp + 1
            else: 
                temp= temp + 0
            if b == 1:
                temp = temp + 2
            else: 
                temp= temp + 0
            if c == 1:
                temp = temp + 4
            else: 
                temp= temp + 0
            if d == 1:
                temp = temp + 8
            else:
                temp= temp + 0
            #Agregamos validaciones para colocar las debidas letras al Hexadecimal
            if temp == 10:
                hex = "A" + hex
            elif temp == 11:
                hex = "B" + hex
            elif temp == 12:
                hex = "C" + hex
            elif temp== 13:
                hex = "D" + hex
            elif temp == 14:
                hex = "E" + hex
            elif temp == 15:
                hex = "F" + hex
            else:
                hex = str(temp) + hex   
            
            mientras = ""
        
        #Logramos obtener el numero!!!!!
        return hex





                
            
            


        

    
    
    



numero = Binario("11110111011101")
print(numero.BinToHex())

 