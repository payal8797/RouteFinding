import json,ast

def notMoreThan3Cities(timeTaken):
    hours=0
    cities=0
    hours+=timeTaken
    cities+=1
    if (hours>24) or (cities==3):
        hours-=24
        cities=0
    if (hours<24) and (cities>3):
        print("Travelled more than 3 cities in a day.")
        hours-=24
    return hours

def zoneTime(city):
    data=open("inputZones.txt","r").read().split("\n")
    t=0
    search=city
    for i in data:
        if search in i and "Red" in i:
            t+=24            
        if search in i and "Orange" in i:
            t+=12
        if search in i and "Green" in i:
            t+=0
    return t

def heuristicFromZone(city):
    data=open("inputZones.txt","r").read().split("\n")
    h=0
    search=city
    for i in data:
        if search in i and "Red" in i:
            h+=24            
        if search in i and "Orange" in i:
            h+=12
        if search in i and "Green" in i:
            h+=0
    return h

def nextCity(frontierList):
    n=len(frontierList)
    array=[]
    temp=0
    min=1000000000
    for i in range(n):
        heuristicvalue=frontierList[i][1][1]+ frontierList[i][1][0]+ heuristicFromZone(frontierList[i][0])
        if heuristicvalue<min:
            min=heuristicvalue 
            temp=i
    return frontierList[temp]

def findFrontier(explored,subData):
    frontier=[]
    for key,value in subData.items():
        array1=[]
        if key in explored:
            subData.pop(key)
            continue
        for key1,value1 in value.items():
            array1.append(value1)
        frontier.append([key,array1])
    return frontier

def route(start,end,data):
    explored=[]
    timeTaken=0
    explored.append(start)
    while(explored[-1]!=end):
        source=explored[-1]
        subData=data[source]
        if end in subData.keys():
            explored.append(end)
            timeTaken+=3+zoneTime(end)
            #print(end,next1[0],next1[1][0],zoneTime(end),timeTaken)
            notMoreThan3Cities(timeTaken)
            break
        else:
            frontierList=findFrontier(explored,subData)
            next1=nextCity(frontierList)
            timeTaken+=next1[1][1]+zoneTime(next1[0])
            #print(next1[0],next1[1][1],zoneTime(next1[0]),timeTaken)
            notMoreThan3Cities(timeTaken)
            explored.append(next1[0])
    return timeTaken,explored
    

if __name__=="__main__":
    start=raw_input("Enter source city : ")
    end="Chandrapur"
    print("Destination : %s" %end)
    fp=open("StateGraph.json",)
    data=json.load(fp)
    data = ast.literal_eval(json.dumps(data))
    subData=data[start]
    timeTaken,explored=route(start,end,data)
    totalTime=120
    if (timeTaken>totalTime):
        print("\nCannot reach in the desired time.\nRequired time=%dhrs .\nPath: %s\n " %(timeTaken,explored))
        print("Total cities travelled: %d\n"%len(explored))
    else:
        print("\nRequired time=%d hrs.\nPath: %s\n " %(timeTaken,explored))
        print("Total cities travelled: %d\n"%len(explored))