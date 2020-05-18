---Route Finding----

To run the code, enter the command: 
    make output


**IMPORTANT POINTS**
1. Make sure while entering the source city, **first alphabet is capital** (Pune/Ahmednagar)
2. Make sure you open the terminal at the same location as of all the other files.


---Explanation---
1. A* algorithem is used to find the optimal path.
2. Map of maharashtra is used to solve the problem.
3. Calculation of heurisic function (h): Sum of the mention 3 points. Values are rounded off 
    1. Direct distance between the source city and destination divided by 60.
    2. Distance between the directly connected cities divided by 60.
    3.  1. if city explored is in Red Zone:
            h+=24
        2. if city explored is in Orange Zone:
            h+=12
        3. if city explored is in Green Zone:
            h+=0
4. The direct distance between any 2 cities(if exists) is stored in the json file StateGraph.json, there is no need of changing anything.
5. The Red/Orange/Green zones are as per today's data in the file inputZones.txt. You can change it as per the requirement.Make sure while enterining the Colour, **first alphabet is capital**(Red/Orange/Green).