#Definicoes das jogadas (esquerda/direita/baixo/cima)
def left(A):
    K=copy(A)
    for i in range(len(K)):
        for j in range(len(K)):
            if (j!=0 and K[i][j]==0):
                K[i][j]=K[i][j-1]
                K[i][j-1]=0
                return K
    return K
  
  
def right(A):
    K=copy(A)
    for i in range(len(K)):
        for j in range(len(K)):
            if (j!=len(K[i])-1 and K[i][j]==0):
                K[i][j]=K[i][j+1]
                K[i][j+1]=0
                return K
    return K
  
  
def down(A):
    K=copy(A)
    for i in range(len(K)):
        for j in range(len(K)):
            if (i!=len(K[i])-1 and K[i][j]==0):
                K[i][j]=K[i+1][j]
                K[i+1][j]=0
                return K
    return K
  
  
def up(A):
    K=copy(A)
    for i in range(len(K)):
        for j in range(len(K)):
            if (i!=0 and K[i][j]==0):
                K[i][j]=K[i-1][j]
                K[i-1][j]=0
                return K
    return K
