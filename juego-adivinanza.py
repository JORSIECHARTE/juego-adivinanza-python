

import random

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 8
adivinado = False



print("!Bienvenido al juego de adivinar el numero secreto!")

while not adivinado:
     if not cant_intentos < cant_max_intentos:
       print("!Game Over! No has podido adivinar dentro de los 8 intentos")
       break
     
     numero = int(input("Introduce un numero del 1 al 99: ")) 
            
     if numero == numero_secreto:
            print("!Felicitaciones has adivinado el numero secreto!")
            adivinado = True
     elif numero < numero_secreto:
            print("el numero es mayor al ingresado")
     else:
            print("El numero es menor al ingresado")

     cant_intentos += 1



   
