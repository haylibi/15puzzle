from auxiliar_functions import *


#Implementacao dos comandos para as buscas diferentes
def makedescendants(node,visited_nodes):
    '''Partindo dum vertice arbitrario, este comando gera uma lista com todos os vertices a que este se liga'''
    A=[['l',left(node)],['r',right(node)],['d',down(node)],['u',up(node)]]
    K=[]
    for i in range(len(A)):
       X = find_aux(A[i][1],visited_nodes)
       if X == []:
           K.append(A[i])
    return K

def findpath(vnodes,configFinal,path):
    visited_nodes=copy(vnodes)
    A=find_aux(configFinal,visited_nodes)
    visited_nodes.remove([A,configFinal])
    if A=='u':
        path.append('u')
        return findpath(visited_nodes,down(configFinal),path)
    if A=='d':
        path.append('d')
        return findpath(visited_nodes,up(configFinal),path)
    if A=='r':
        path.append('r')
        return findpath(visited_nodes,left(configFinal),path)
    if A=='l':
        path.append('l')
        return findpath(visited_nodes,right(configFinal),path)
    else:
        return path


#Busca de largura (breadth first search)
def bfs(configInicial,configFinal):
    tempo=time.time()
    visited_nodes=[]
    if not(is_solvable(configInicial,configFinal)):
        return "It is impossible to reach a solution"
    configFinal = configFinal.split(' ')
    configFinal = str2int(configFinal)
    configFinal =[configFinal[:4]]+[configFinal[4:8]]+[configFinal[8:12]]+[configFinal[12:]]
    configInicial = configInicial.split(' ')
    configInicial = str2int(configInicial)
    configInicial=[configInicial[:4]]+[configInicial[4:8]]+[configInicial[8:12]]+[configInicial[12:]]
    if configInicial == configFinal:
        return 'Inicial configuration is the same as the final one'
    visited_nodes.append(['',configInicial])
    descendants = makedescendants(configInicial,visited_nodes)
    return bfs_2(descendants ,configFinal,visited_nodes,tempo)
def bfs_2(configInicial,configFinal,vnodes,tempo):      #Caso onde configInicial tem a última jogada na lista e configFinal está em forma de matriz
    queue = copy(configInicial)
    visited_nodes=copy(vnodes)
    while queue !=[]:
        node = queue[0][1]
        K = copy2([queue[0][0],node])
        queue = queue[1:]
        visited_nodes.append(K)
        if node == configFinal:
            path=findpath(visited_nodes,configFinal,[])
            path=invert_list(path)
            return 'Movements from Inicial to Final:',path,'Seconds it took:', time.time()-tempo, 'Space used:',len(visited_nodes)
    descendants=[]
    for i in range(len(configInicial)):
        descendants+=makedescendants(configInicial[i][1],visited_nodes)
    if descendants == []:
        return 'Solution not found'
    return bfs_2(descendants,configFinal,visited_nodes,tempo)

#Busca em Profundidade
def depthfirst(configInicial,configFinal,max_depth):
    '''configInicial -> configuração Inicial; configFinal -> configuração final; max_depth-> nivel de profundidade desejada'''
    tempo=time.time()
    visited_nodes=[]
    if not(is_solvable(configInicial,configFinal)):
        return "It is impossible to reach a solution"
    configFinal = configFinal.split(' ')
    configFinal = str2int(configFinal)
    configFinal =[configFinal[:4]]+[configFinal[4:8]]+[configFinal[8:12]]+[configFinal[12:]]
    configInicial = configInicial.split(' ')
    configInicial = str2int(configInicial)
    configInicial=[configInicial[:4]]+[configInicial[4:8]]+[configInicial[8:12]]+[configInicial[12:]]
    if configInicial == configFinal:
        return 'Your inicial state is the same as the final one, so no calculation is needed.'
    descendants = makedescendants(configInicial,visited_nodes)
    visited_nodes.append(['',configInicial])
    return depthfirst2(descendants,configFinal,visited_nodes,tempo,[],max_depth,0,len(visited_nodes))

def depthfirst2(configInicial,configFinal,vnodes,tempo,path,max_depth,depth,memory):
    path.append([])
    queue = copy(configInicial)
    visited_nodes = copy(vnodes)
    visited_nodes.append([])
    if depth>=max_depth:
        return memory
    while queue!=[]:
        node = queue[0][1]
        visited_nodes[-1] = [queue[0][0],node]
        path[-1] = queue[0][0]
        queue = queue[1:]
        memory = max(len(visited_nodes),memory)
        if node == configFinal:
            return 'Movements from Inicial to Final:',path,'Seconds it took:',time.time()-tempo,'Maximum space used:',memory
        descendant = makedescendants(node,visited_nodes)
        p = copia(path)
        A = depthfirst2(descendant,configFinal,visited_nodes,tempo,p,max_depth,depth+1,memory)
        if type(A) != int:
            return A
        memory = A
    if depth == 0:
        return 'Solution not found'
    return memory

def depth_firsti(configInicial,configFinal):
    tempo=time.time()
    visited_nodes=[]
    if not(is_solvable(configInicial,configFinal)):
        return "It is impossible to reach a solution"
    configFinal = configFinal.split(' ')
    configFinal = str2int(configFinal)
    configFinal =[configFinal[:4]]+[configFinal[4:8]]+[configFinal[8:12]]+[configFinal[12:]]
    configInicial = configInicial.split(' ')
    configInicial = str2int(configInicial)
    configInicial=[configInicial[:4]]+[configInicial[4:8]]+[configInicial[8:12]]+[configInicial[12:]]
    if configInicial == configFinal:
        return 'Your inicial state is the same as the final one, so no calculation is needed.'
    descendants = makedescendants(configInicial,visited_nodes)
    visited_nodes.append(['',configInicial])
    max_depth = 0
    while True:
        A = depthfirst2(descendants,configFinal,visited_nodes,tempo,[],max_depth,0,len(visited_nodes))
        if not(type(A) == int or A == 'Solution not found'):
            return A
        max_depth += 1


def heuristic1(configInicial,configFinal):
    '''configurações em forma de matriz, retorna o número de peças fora do sítio'''
    count = 0
    for i in range(len(configInicial)):
        for j in range(len(configInicial)):
            if (configInicial[i][j]!=configFinal[i][j] and configInicial[i][j] != 0):
                count+=1
    return count

def heuristic2(configInicial,configFinal):
    '''tendo as configurações em formas de matrizes, retorna o valor da função heuristica manhattan'''
    k = 0
    positions1=[]
    positions2=[]
    temp = []
    for i in range(len(configInicial)):
        for j in range(len(configInicial)):
            positions1.append([[i,j],configInicial[i][j]])
    for i in range(len(configFinal)):
        for j in range(len(configFinal)):
            positions2.append([[i,j],configFinal[i][j]])
    for i in range(len(positions1)-1):
        P1=find_aux(i+1,positions1)
        P2=find_aux(i+1,positions2)
        temp.append(abs(P2[0]-P1[0])+abs(P2[1]-P1[1]))
    return sum(temp)

def makedescendants_h1(node,configFinal,visited_nodes,v2):
    '''Partindo dum vertice arbitrario, este comando gera uma lista com todos os vertices a que este se liga utilizando a funcao heuristica 1'''
    e = left(node)
    d = right(node)
    b = down(node)
    c = up(node)
    A=[['l',e,heuristic1(e,configFinal)],['r',d,heuristic1(d,configFinal)],['d',b,heuristic1(b,configFinal)],['u',c,heuristic1(c,configFinal)]]
    K=[]
    for i in range(len(A)):
       X = find_aux(A[i][1],visited_nodes)
       Y = find_aux(A[i][1],v2)
       if (X == [] and Y == []):
           K.append(A[i])
    return K
def makedescendants_h2(node,configFinal,visited_nodes,v2):
    '''Partindo dum vertice arbitrario, este comando gera uma lista com todos os vertices a que este se ligautilizando a funcao heuristica 2'''
    e = left(node)
    d = right(node)
    b = down(node)
    c = up(node)
    A=[['l',e,heuristic2(e,configFinal)],['r',d,heuristic2(d,configFinal)],['d',b,heuristic2(b,configFinal)],['u',c,heuristic2(c,configFinal)]]
    K=[]
    for i in range(len(A)):
       X = find_aux(A[i][1],visited_nodes)
       Y = find_aux(A[i][1],v2)
       if (X == [] and Y == []):
           K.append(A[i])
    return K

def sort(descendants):
    '''vai ordenar os vértices de forma a que o com o valor menor de heuristica seja o primeiro a ser visitado'''
    for iter_num in range(len(descendants)-1,0,-1):
        for idx in range(iter_num):
            if descendants[idx][2]>descendants[idx+1][2]:
                temp = descendants[idx][2]
                descendants[idx][2] = descendants[idx+1][2]
                descendants[idx+1][2] = temp
    return descendants
def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0][2] < right_half[0][2]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

def greedy_h1(configInicial,configFinal):
    tempo=time.time()
    visited_nodes=[]
    if not(is_solvable(configInicial,configFinal)):
        return "It is impossible to reach a solution"
    configFinal = configFinal.split(' ')
    configFinal = str2int(configFinal)
    configFinal =[configFinal[:4]]+[configFinal[4:8]]+[configFinal[8:12]]+[configFinal[12:]]
    configInicial = configInicial.split(' ')
    configInicial = str2int(configInicial)
    configInicial=[configInicial[:4]]+[configInicial[4:8]]+[configInicial[8:12]]+[configInicial[12:]]
    h1 = heuristic1(configInicial,configFinal)
    visited_nodes.append(['',configInicial])
    descendants = sort(makedescendants_h1(configInicial,configFinal,visited_nodes,visited_nodes))
    return greedy2_h1(descendants ,configFinal,visited_nodes,tempo)
def greedy2_h1(configInicial,configFinal,vnodes,tempo):      #Caso onde configInicial tem a última jogada na lista e configFinal está em forma de matriz
    visited_nodes=copy(vnodes)
    while True:
        node = configInicial[0][1]
        K = copy2([configInicial[0][0],node])
        configInicial = configInicial[1:]
        visited_nodes.append(K)
        if node == configFinal:
            path=findpath(visited_nodes,configFinal,[])
            path=invert_list(path)
            return 'Movements from Inicial to Final:',path,'Seconds it took:', time.time()-tempo, 'Space used:',max(len(visited_nodes),len(configInicial))
        configInicial = merge(configInicial,sort(makedescendants_h1(node, configFinal,visited_nodes,configInicial)))

def greedy_h2(configInicial,configFinal):
    tempo=time.time()
    visited_nodes=[]
    if not(is_solvable(configInicial,configFinal)):
        return "It is impossible to reach a solution"
    configFinal = configFinal.split(' ')
    configFinal = str2int(configFinal)
    configFinal =[configFinal[:4]]+[configFinal[4:8]]+[configFinal[8:12]]+[configFinal[12:]]
    configInicial = configInicial.split(' ')
    configInicial = str2int(configInicial)
    configInicial=[configInicial[:4]]+[configInicial[4:8]]+[configInicial[8:12]]+[configInicial[12:]]
    h2 = heuristic2(configInicial,configFinal)
    visited_nodes.append(['',configInicial])
    descendants = sort(makedescendants_h2(configInicial,configFinal,visited_nodes,visited_nodes))
    return greedy2_h2(descendants ,configFinal,visited_nodes,tempo)
def greedy2_h2(configInicial,configFinal,vnodes,tempo):      #Caso onde configInicial tem a última jogada na lista e configFinal está em forma de matriz
    visited_nodes=copy(vnodes)
    while True:
        node = configInicial[0][1]
        K = copy2([configInicial[0][0],node])
        configInicial = configInicial[1:]
        visited_nodes.append(K)
        if node == configFinal:
            path=findpath(visited_nodes,configFinal,[])
            path=invert_list(path)
            return 'Movements from Inicial to Final:',path,'Seconds it took:', time.time()-tempo, 'Space used:',max(len(visited_nodes),len(configInicial))
        configInicial = merge(configInicial,sort(makedescendants_h2(node, configFinal,visited_nodes,configInicial)))


def makedescendants2_h1(node,configFinal,visited_nodes,v2,real_path):
    '''Partindo dum vertice arbitrario, este comando gera uma lista com todos os vertices a que este se liga  utilizando a funcao heuristica 1 + valor no pai'''
    e = left(node[0])
    d = right(node[0])
    b = down(node[0])
    c = up(node[0])
    A=[['l',e,real_path+heuristic1(e,configFinal)],['r',d,real_path+heuristic1(d,configFinal)],['d',b,real_path+heuristic1(b,configFinal)],['u',c,real_path+heuristic1(c,configFinal)]]
    K=[]
    for i in range(len(A)):
       X = find_aux(A[i][1],visited_nodes)
       Y = find_aux(A[i][1],v2)
       if (X == [] and Y == []):
           K.append(A[i])
    return K
def makedescendants2_h2(node,configFinal,visited_nodes,v2):
    '''Partindo dum vertice arbitrario, este comando gera uma lista com todos os vertices a que este se liga  utilizando a funcao heuristica 2 + valor no pai'''
    e = left(node[0])
    d = right(node[0])
    b = down(node[0])
    c = up(node[0])
    A=[['l',e,node[1]+heuristic2(e,configFinal)],['r',d,node[1]+heuristic2(d,configFinal)],['d',b,node[1]+heuristic2(b,configFinal)],['u',c,node[1]+heuristic2(c,configFinal)]]
    K=[]
    for i in range(len(A)):
       X = find_aux(A[i][1],visited_nodes)
       Y = find_aux(A[i][1],v2)
       if (X == [] and Y == []):
           K.append(A[i])
    return K

def Astar_h1(configInicial,configFinal):
    tempo=time.time()
    visited_nodes=[]
    if not(is_solvable(configInicial,configFinal)):
        return "It is impossible to reach a solution"
    configFinal = configFinal.split(' ')
    configFinal = str2int(configFinal)
    configFinal =[configFinal[:4]]+[configFinal[4:8]]+[configFinal[8:12]]+[configFinal[12:]]
    configInicial = configInicial.split(' ')
    configInicial = str2int(configInicial)
    configInicial=[configInicial[:4]]+[configInicial[4:8]]+[configInicial[8:12]]+[configInicial[12:]]
    h1 = heuristic1(configInicial,configFinal)
    visited_nodes.append(['',configInicial])
    descendants = sort(makedescendants2_h1([configInicial,0],configFinal,visited_nodes,visited_nodes,0))
    return Astar2_h1(descendants ,configFinal,visited_nodes,tempo)
def Astar2_h1(configInicial,configFinal,vnodes,tempo):      #Caso onde configInicial tem a última jogada na lista e configFinal está em forma de matriz
    visited_nodes=copy(vnodes)
    real_path=0
    while True:
        heuristic = configInicial[0][2]
        node = configInicial[0][1]
        K = copy2([configInicial[0][0],node])
        configInicial = configInicial[1:]
        visited_nodes.append(K)
        if node == configFinal:
            path=findpath(visited_nodes,configFinal,[])
            path=invert_list(path)
            return 'Movements from Inicial to Final:',path,'Seconds it took:', time.time()-tempo, 'Space used:',max(len(visited_nodes),len(configInicial))
        configInicial = merge(configInicial,sort(makedescendants2_h1([node,heuristic], configFinal,visited_nodes,configInicial,real_path)))
        real_path+=1
        

def Astar_h2(configInicial,configFinal):
    tempo=time.time()
    visited_nodes=[]
    if not(is_solvable(configInicial,configFinal)):
        return "It is impossible to reach a solution"
    configFinal = configFinal.split(' ')
    configFinal = str2int(configFinal)
    configFinal =[configFinal[:4]]+[configFinal[4:8]]+[configFinal[8:12]]+[configFinal[12:]]
    configInicial = configInicial.split(' ')
    configInicial = str2int(configInicial)
    configInicial=[configInicial[:4]]+[configInicial[4:8]]+[configInicial[8:12]]+[configInicial[12:]]
    h1 = heuristic1(configInicial,configFinal)
    visited_nodes.append(['',configInicial])
    descendants = sort(makedescendants2_h2([configInicial,0],configFinal,visited_nodes,visited_nodes))
    return Astar2_h2(descendants ,configFinal,visited_nodes,tempo)
def Astar2_h2(configInicial,configFinal,vnodes,tempo):      #Caso onde configInicial tem a última jogada na lista e configFinal está em forma de matriz
    visited_nodes=copy(vnodes)
    while True:
        heuristic = configInicial[0][2]
        node = configInicial[0][1]
        K = copy2([configInicial[0][0],node])
        configInicial = configInicial[1:]
        visited_nodes.append(K)
        if node == configFinal:
            path=findpath(visited_nodes,configFinal,[])
            path=invert_list(path)
            return 'Movements from Inicial to Final:',path,'Seconds it took:', time.time()-tempo, 'Space used:',max(len(visited_nodes),len(configInicial))
        configInicial = merge(configInicial,sort(makedescendants2_h2([node,heuristic], configFinal,visited_nodes,configInicial)))
