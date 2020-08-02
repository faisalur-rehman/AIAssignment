stateDescriptions=[]
rules=[]
inputFile=[]
transitionTable=None
testCases=[]
frontier=[]
parentData=[]
exploredSet=[]

file=open('input.txt','r')

inputFile.append(file.readline())

noOfStates=int(inputFile[0].split()[0],10)

noOfRules=int(inputFile[0].split()[1],10)

noOfTestCases=int(inputFile[0].split()[2],10)
rows, cols = (noOfStates,noOfRules)
transitionTable =[[0 for i in range(cols)] for j in range(rows)]


def checkExplored(dequ):
    for x in range(len(exploredSet)):
        if(exploredSet[x]==dequ):
            return True
    return False