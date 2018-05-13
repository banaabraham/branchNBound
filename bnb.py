import math



#koordinat =  [[200,129],[442,325],[443,33],[240,430],[300,615],[240,430]]
file = open("C:\\Users\\lenovo\\Desktop\\coding practice\\ganjar\\mymungit.github.io-master\\mymungit.github.io-master\\example.csv")

koordinat = []
for i in file:
    temp = i.replace("\n","").split(",")
    koordinat.append([int(temp[1]),int(temp[2])])

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def alldistance(jalur):
    dis = 0
    for i in range(len(jalur)-1):
        dis += distance(koordinat[jalur[i]],koordinat[jalur[i+1]])
    return dis


def genCostMat(koordinat):
    costMat = [[0 for i in range(len(koordinat))] for i in range(len(koordinat))]
    for i in range(len(koordinat)):
        for j in range(len(koordinat)):
            if i==j:
                costMat[i][j] = float('Inf')
            else:
                costMat[i][j] = distance(koordinat[i],koordinat[j])
    return costMat

def reduce(costMat,adder=0):
    minRow = []
    cols = [[] for i in range(len(koordinat))]
    minCol = []
    reduced = [[0 for i in range(len(koordinat))] for i in range(len(koordinat))]
    for row in costMat:
        mr = min(row)
        if mr==float('Inf'):
            minRow.append(0)
        else:
            minRow.append(mr)
    
    #reduce row
    for i in range(len(costMat)):
        for j in range(len(costMat)):
            reduced[i][j] = costMat[i][j] - minRow[i]
            
    for row in reduced:
        for i in range(len(row)):
            cols[i].append(row[i])  
    #find minCol
    for i in cols:
        mc = min(i)
        if mc==float('Inf'):
            minCol.append(0)
        else:
            minCol.append(mc)
        
    #reduce column
    for i in range(len(costMat)):
        for j in range(len(costMat)):
            reduced[i][j] = reduced[i][j] - minCol[j]
 
    cost = sum(minRow)+sum(minCol)+adder
    return reduced,cost

def evaluate(cm,x,y):
    transformed = [[0 for i in range(len(koordinat))] for i in range(len(koordinat))]
    
    for i in range(len(koordinat)):
        for j in range(len(koordinat)):
            if i==x or j==y:
                transformed[i][j] = float('Inf')
            else:
                transformed[i][j] = cm[i][j]
    return transformed

def getNext(awal,cm,cities):
    Next = []
    newCm = []
    Min = float("Inf")
    for i in cities: 
        if i!=awal:
            temp = evaluate(cm,awal,i)
            m,c = reduce(temp,cost_matrix[awal][i])
            if c<Min:
                Min = c
                Next = i   
                newCm = temp
    return Next,newCm,Min


def solve(koordinat):
    cities = [i for i in range(len(koordinat))]
    awal = 0
    jalur = [awal]
    
    cities.remove(0)
    
    m = genCostMat(koordinat)
    cm,Min = reduce(m)
    global cost_matrix
    cost_matrix = cm
    
    while len(cities)>0:
        temp = getNext(awal,cm,cities)
        jalur.append(temp[0])
        cm = temp[1]
        awal = temp[0]
        cities.remove(awal)
    
    jalur.append(0)  
        
    return jalur

cost_matrix = []

j = solve(koordinat)
t = [i for i in range(len(koordinat))]
print(alldistance(j)) 
print(alldistance(t)) 
