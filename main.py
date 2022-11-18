import random
'''def multiMatriz(m1, m2):
    m3 = []
    for i in range(len(m1[0])):
        m3.append([])
        for j in range(len(m2)):
            m3[i].append(0)
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m1[0])):
                m3[i][j] += m1[i][k] * m2[k][i]
    return m3'''
def multiMatriz(m1,m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0)
    for r in range(len(m1)):
        for c in range(len(m2[0])):
            for k in range(0, len(m2)):
                m3[r, c] += m1[r, k]*m2[k, c]
    return m3
# -----------------------------------------------
def esIgual(m1,m2,m3):
    if m3 == multiMatriz(m1,m2):
        return True
    else:
        return False
def freivalds(m1,m2,m3,n):
    X = []
    for i in range(n):
        X.append([])
        for j in range(n):
            X[i].append(random.randint(0, 1))
    if multiMatriz((multiMatriz(X,m1)),m2) == multiMatriz(X,m3):
        return True
    else:
        return False
A = [[69, 31, 75], [64, 7, 94], [34, 18, 26]]
B = [[34, 18, 26], [64, 7, 94], [69, 31, 75]]
C = multiMatriz(A,B)
#C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Resultado A x B =",multiMatriz(A,B))
print("C: ",C)
print("Es igual? :",esIgual(A,B,C))
print("freivalds? :",freivalds(A,B,C,len(A[0])))