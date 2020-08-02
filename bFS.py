from config import *
from getChildren import *


def findPlan(source,goal):
    plan=[]
    plan.clear()
    while(source!=goal):
        for x in range(len(parentData)):
            if(parentData[x]['child']==goal):
                #print(parentData[x]['rule'])
                plan.append(parentData[x]['rule'])
                goal=parentData[x]['parent']
                break
    count=len(plan)
    for x in range(count):
        if(x==count-1):

            print(rules[plan.pop()])
        else:
            print(rules[plan.pop()],end="->")

    print("")


def bFS(testCases):

    for y in range(len(testCases)):
        print("TEST CASE ",y+1," :", end =" ")
        parentData.clear()
        frontier.clear()
        goalFound=False
        exploredSet.clear()
        frontier.append(testCases[y]['initial'])
        if(testCases[y]['initial']==testCases[y]['final']):
            print('Do Nothing')
        else:
            while(len(frontier)!=0 ):
                if(goalFound==True):
                    break
                dequed=frontier.pop(0)
                exploredSet.append(dequed)

                children=getChildren(dequed)
                for x in range(len(children)):
                    if(children[x]==testCases[y]['final']):
                        goalFound=True
                    else:
                        temp=checkExplored(children[x]);
                        if(temp==False):
                            frontier.append(children[x])


            if(len(frontier)==0 and goalFound==False):
                print("GOAL NOT FOUND")
            else:
                print("GOAL FOUND")
                print("PLAN : ", end =" ")
                findPlan(testCases[y]['initial'],testCases[y]['final'])

