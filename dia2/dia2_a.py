codigoBinario = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0]
codigoBinario[1]=12
codigoBinario[2]=2
#codigoBinario[0]=4
# avanzamos de 4 en 4
def leerBinario(listado):
    L = listado
    POS = 0
    lon = len(L)
    #print("longitud de la lista: ", lon) # lon -1 para referirse a la posición de la lista
    #print("Posición actual: ", POS)
    numero1 = 0
    numero2 = 0
    numero3 = 0
    for X in range(0, len(L), 4): # aquí ya leo por cuartetos
        if L[X] == 99:            
            return L

        numero1 = L[X+1] # Posicion de numero 1
        numero2 = L[X+2] # Posicion de numero 2
        numero3 = L[X+3] # Posicion de numero 3

        if L[X] == 1:
            L[numero3] = L[numero1] + L[numero2]
            #print("#1 ", L[numero1], " + #2 ", L[numero2], " = ", L[numero1] + L[numero2])
            continue
        if L[X] == 2:
            L[numero3] = L[numero1] * L[numero2]
            #print("#1 ", L[numero1], " * #2 ", L[numero2], " = ", L[numero1] * L[numero2])

print("Lista inicial: ", codigoBinario)
print("Lista Modificada: ", leerBinario(codigoBinario) )
print("Valor de la casilla 1: ", codigoBinario[0])
# 5866663