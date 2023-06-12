import time
import math

#Definicoes auxiliares
def member(a,b):
    '''Verifica se "a" e um membro de uma lista b'''
    for i in b:
        if a==i:
            return True
    return False
def find_aux(A,B):
    '''Verifica se "A" e um membro de B, onde B e uma lista cujos elementos sao da forma [p,v] onde v e um vertice do grafo e p o seu respetivo pai'''
    for i in B:
        if A==i[1]:
            return i[0]
    return []
def str2int(A):
    '''converte uma lista com elementos em string para uma com elementos em inteiros (desde que sejam numeros)'''
    L=[]
    for i in A:
        L.append(int(i))
    return L
def invert_list(A):
    '''Inverte uma lista A (para obter o caminho pretendido)'''
    K=[]
    for i in range(len(A)):
        K.append(A[-1-i])
    return K
#Inicio do codigo
def inverse(a,b):
    '''Verifica as inversoes de "a" na lista "b"'''
    count=0
    for i in b:
        if type(i)==int:
            if i!=0:
                if a>i:
                    count+=1
    return count
def par(A):
    '''Verifica a paridade de uma configuracao A'''
    L=[]
    count=0
    inv=0
    blankrow=0
    for i in A:
        if member(0,i):
            blankrow=4-count
        for k in i:
            L.append(k)
        count+=1
    for i in range(len(L)):
        inv+=inverse(L[i],L[i:])
    return (inv%2)==(blankrow%2)
def is_solvable(A,B):
    '''Vai testar se e possivel passar da config A para B (funciona com lista de listas ou uma sting em cadeia, como pedido)'''
    if type(A)==type(B)==list:
        return par(A)==par(B)
    A=str2int(A.split())
    B=str2int(B.split())
    A1=[A[:4]]+[A[4:8]]+[A[8:12]]+[A[12:]]
    B1=[B[:4]]+[B[4:8]]+[B[8:12]]+[B[12:]]
    return par(A1)==par(B1)


#Definicoes de copias de listas (para nao haver erros na execucao do codigo)
def copy(A):
    '''copia para executar os movimentos (estava a alterar o vertice depois da jogada)'''
    K = []
    for i in range(len(A)):
        K.append([])
        for j in range(len(A[i])):
            K[i].append(0)
            K[i][j] = A[i][j]
    return K
def copy2(A):
    K = []
    for i in range(len(A)):
        K.append([])
        for j in range(len(A[i])):
            K[i].append(0)
            K[i][j] = A[i][j]
    K[0]=A[0]
    return K
def copia(n):
    A=[]
    for i in range(len(n)):
        A.append([])
        A[i] = n[i]
    return A
