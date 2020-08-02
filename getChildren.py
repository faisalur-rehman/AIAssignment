
from config import*




def getStateNumber(deque):
    for x in range(noOfStates):
        if(stateDescriptions[x]==deque):
            return (x)

def getChildren(deque):

    stateNumber= getStateNumber(deque)
    
    children=[]
    actions=[]
    for x in range(noOfRules):
        if(int(transitionTable[stateNumber][x],10)!=stateNumber):
            children.append(stateDescriptions[int(transitionTable[stateNumber][x],10)])
            temp={'child':stateDescriptions[int(transitionTable[stateNumber][x],10)],'parent':deque,'rule':x}
            parentData.append(temp)
    return children