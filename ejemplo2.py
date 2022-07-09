import sys

if len(sys.argv) !=3: #Si la longitud de la lista es distinto de 3
    print("error, necesito 2 argumentos")
else:
    for i in range(int(sys.argv[2])): #el parametro 2 debe ser un entero y se va a replicar n cantidad de veces el parametro 1 (que es es el string)
        print(sys.argv[1])

