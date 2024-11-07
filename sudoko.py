##########entrada#########1111111111
cont = 0
matriz = []
while cont != 9:
    matriz.append(input())
    cont = cont +1
##############################################
quadrado = {}
for i in range(0,9):
    for j in range(1,19,2):
        if matriz[i][j] == " ":
            LC = str(i)+':' +str(j)
            quadrado[LC] = []
            ######################
for i in quadrado:
    for n in range(1,10):
        quadrado[i].append(n)
def main():    
    for i in quadrado:
        for n in quadrado[i].copy():
            for j in range(1,19,2):
                if matriz[int(i[0])][j]==str(n):
                    quadrado[i].remove(n)
            for j in range(0,9):
                if matriz[j][int(i[2:])]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==0 and int(i[2:])%3 ==1:
                if matriz[int(i[0])+1][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])+4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+2][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+2][int(i[2:])+4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==0 and int(i[2:])%3 ==0:
                if matriz[int(i[0])+1][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])+2]==str(n)and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+2][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+2][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==0 and int(i[2:])%3 ==2:
                if matriz[int(i[0])+1][int(i[2:])-4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+2][int(i[2:])-4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+2][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==1 and int(i[2:])%3 ==1:
                if matriz[int(i[0])+1][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])+4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-1][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-1][int(i[2:])+4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==1 and int(i[2:])%3 ==0:
                if matriz[int(i[0])-1][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-1][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==1 and int(i[2:])%3 ==2:
                if matriz[int(i[0])+1][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])-4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])+1][int(i[2:])-4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==2 and int(i[2:])%3 ==1:
                if matriz[int(i[0])-1][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-1][int(i[2:])+4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-2][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-2][int(i[2:])+4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==2 and int(i[2:])%3 ==0:
                if matriz[int(i[0])-1][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-1][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-2][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-2][int(i[2:])+2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
            if int(i[0])%3==2 and int(i[2:])%3 ==2:
                if matriz[int(i[0])-1][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-1][int(i[2:])-4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-2][int(i[2:])-2]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
                if matriz[int(i[0])-2][int(i[2:])-4]==str(n) and n in quadrado[i]:
                    quadrado[i].remove(n)
########critério da unicidade####################
    for i in quadrado:
        if len(quadrado[i])==1:
            matriz[int(i[0])] = matriz[int(i[0])][:int(i[2:])]+str(quadrado[i][0])+ matriz[int(i[0])][(int(i[2:])+1):]
            main()
################critério das linhas#################
    linha = {}
    for n in range(0,9):
        linha[str(n)] = []
        for i in quadrado:
            if n == int(i[0]):
                for t in quadrado[i]:
                    linha[str(n)].append(t)
    for i in linha:
        for n in range(0,10):
            cont = 0
            for t in linha[i]:
                if n==int(t):
                    cont = cont+1
            if cont== 1:
                for k in quadrado:
                    if i == k[0]:
                        for h in quadrado[k]:
                            if int(h) == n:
                                matriz[int(k[0])] = matriz[int(k[0])][:int(k[2:])]+str(quadrado[k][0])+ matriz[int(k[0])][(int(k[2:])+1):]
                                quadrado[k].remove(n)
                                main()    
##################criterio das colunas###############
    coluna = {}
    for n in range(1,19,2):
        coluna[str(n)] = []
        for i in quadrado:
            if n == int(i[2:]):
                for t in quadrado[i]:
                    coluna[str(n)].append(t)
    for i in coluna:
            for n in range(0,10):
                cont = 0
                for t in coluna[i]:
                    if n==int(t):
                        cont = cont+1
                if cont== 1:
                    for k in quadrado:
                        if i == k[2:]:
                            for h in quadrado[k]:
                                if int(h) == n:
                                    matriz[int(k[0])] = matriz[int(k[0])][:int(k[2:])]+str(quadrado[k][0])+ matriz[int(k[0])][(int(k[2:])+1):]
                                    quadrado[k].remove(n)
                                    main()                                    
# #######critério dos quadrantes################
# quadrante = {}
# for n in range(1,10):
    

###########saída########################
#for i in matriz:
   # print(i)


if __name__ == "__main__":
    main()
    for i in matriz:
        print(i)




    
