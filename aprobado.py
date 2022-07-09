import sys

if len(sys.argv) ==3:
    nota1 = float(sys.argv[1])
    nota2 = float(sys.argv[2])

    if nota1>=7 and nota2>=7:
        print("Promocionado")

    elif nota1>=4 and nota2>=4:
        print("Aprobado, debe rendir el final")

    elif (nota1<4 or nota2<4) and (not (nota1<4 and nota2<4)):
        if nota1<4:
            print("Recupera el primer parcial")
        else:
            print("Recupera el segundo parcial")
    else:
        print("Debe recursar")
else:
    print("Error, debe ingresar 2 notas")
