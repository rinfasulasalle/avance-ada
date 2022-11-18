import random
# -----------------------------
def multiMatriz(m1,m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0)
    for r in range(len(m1)):
        for c in range(len(m2[0])):
            for k in range(0, len(m2)):
                #print(r,c,"+=",r,k ,"*",k,c)
                m3[r][c] += (m1[r][k]*m2[k][c])
    return m3
# -----------------------------
def generarMatriz(fila, columna):
    matriz = []
    for i in range(fila):
        matriz.append([])
        for j in range(columna):
            matriz[i].append(random.randrange(0, fila * columna))
    return matriz
# ---------------------------
def main():
    fila = 5
    columna = 3
    m1 = generarMatriz(fila, columna)
    m2=  generarMatriz(columna, fila)
    print(m1)
    print(m2)
    #print("tam de m1:",len(m1),"x",len(m1[0]))
    #print("tam de m2:",len(m2),"x",len(m2[0]))
    print(multiMatriz(m1,m2))
# ---------------------------
main()