def multiMatriz(m1,m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0)
    #print(m3)
    for r in range(len(m1)):
        for c in range(len(m2[0])):
            for k in range(0, m2):
                print(r,c,"+=",r,k ,"*",k,c)
                m3[r, c] += m1[r, k]*m2[k, c]
    return m3
# -----------------------------

# ---------------------------
def main():
    m1 = [
        [1,2],
        [3,4],
        [5,6]]
    m2= [
        [1,2,3],
        [4,5,6]]
    print("tam de m1:",len(m1),"x",len(m1[0]))
    print("tam de m2:",len(m2),"x",len(m2[0]))
    print(multiMatriz(m1,m2))
# ---------------------------
main()