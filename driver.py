from getChildren import*
from config import*


from bFS import *

for x in range(noOfStates):
    stateDescriptions.append(file.readline().rstrip('\n'))

for x in range(noOfRules):
    rules.append(file.readline().rstrip('\n'))

for x in range(noOfStates):
    rowData=file.readline()
    for y in range(noOfRules):
        transitionTable[x][y]=rowData.split()[y]

for x in range(noOfTestCases):
    line=file.readline()
    temp={'initial':line.split(' (')[0],'final':line.split(') ')[1].rstrip('\n')}
    testCases.append(temp)
bFS(testCases)






























