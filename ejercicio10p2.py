print("----------------------------------")
print("Letra                        valor")
print("----------------------------------")
print("A, E, I, O, U, L, N, R, S, T    1")
print("D, G                            2")
print("B, C, M, P                      3")
print("F, H, V, W, Y                   4")
print("K                               5")
print("J, X                            8")
print("Q, Z                            10")
print("----------------------------------")

def leer_palabra():
    global txt
    txt=input("ingrese palabra:")
def contar_valor():
    valor1 = [ "A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    cont1=0
    for i in valor1:
        for j in txt:
            if(i==j):
                cont1+=1    

    valor2 = [ "D", "G"]
    cont2=0
    for i in valor2:
        for j in txt:
            if(i==j):
                cont2+=2   

    valor3 = [ "B", "C", "M", "P"]
    cont3=0
    for i in valor3:
        for j in txt:
            if(i==j):
                cont3+=3   

    valor4 = [ "F", "H", "V", "W", "Y"]
    cont4=0
    for i in valor4:
        for j in txt:
            if(i==j):
                cont4+=4
    
    valor5 = [ "K"]
    cont5=0
    for i in valor5:
        for j in txt:
            if(i==j):
                cont5+=5
    
    valor8 = [ "J", "X"]
    cont8=0
    for i in valor8:
        for j in txt:
            if(i==j):
                cont8+=8    

    valor10 = [ "Q", "Z"]
    cont10=0
    for i in valor10:
        for j in txt:
            if(i==j):
                cont10+=10
    print("valor:",cont1+cont2+cont3+cont4+cont5+cont8+cont10)

leer_palabra()
contar_valor()