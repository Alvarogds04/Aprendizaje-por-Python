
import exportar_excel

while True:
    num = input("Introduce el numero: ")
    if len(num) < 3:
        print("Error: El numero tiene menos de 3 caracteres")
    elif len(num) > 4:
        print("Error: El numero tiene mas de 4 caracteres")
    else:
        break


exportar_excel.guardar(num)

