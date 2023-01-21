a = [[1,2],
     [3,3],
     [5,6]]
b = [[1,2,3],
     [3,4,5]]

def multiplicar_matrices(m1, m2) :
   
    if len(m1[0]) == len(m2) :

        m3 = []
        for i in range(len(m1)):
            m3.append ([])
            for j in range(len(m2[0])):
                m3[i].append(0)

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
        return m3
    else:
        return None
c = multiplicar_matrices(a,b)

if c == None:
    print("nose puede multiplicar ")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")

c.sort(reverse=True)
print(c)

busqueda=input("colocar numero")
print("resultado : ",c.get(busqueda,"no se encontro"))