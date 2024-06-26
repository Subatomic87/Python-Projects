What does this program do?
Basically, farmer John created a teleporter from point x to y, and he is trying to go from point a to b. One step is like from 1 to 2.
The input line is: a b x y
The output line is: the least amount of steps farmer John needs to move

A more detailed problem description is given below.

One of the farming chores Farmer John dislikes the most is hauling around lots of cow manure. In order to streamline this process, he comes up with a brilliant invention: the manure teleporter! Instead of hauling manure between two points in a cart behind his tractor, he can use the manure teleporter to instantly transport manure from one location to another.

Farmer John's farm is built along a single long straight road, so any location on his farm can be described simply using its position along this road (effectively a point on the number line). A teleporter is described by two numbers x and y, where manure brought to location x can be instantly transported to location y, or vice versa.

Farmer John wants to transport manure from location a to location b, and he has built a teleporter that might be helpful during this process (of course, he doesn't need to use the teleporter if it doesn't help). Please help him determine the minimum amount of total distance he needs to haul the manure using his tractor.

Note: install python libraries to run the program.

How to run the program?
1. type the following: 
python teleport_usaco.py
2. Enter four space-separated integers: a and b, describing the start and end locations, followed by x and y, describing the teleporter. All positions are integers in the range 0…100, and they are not necessarily distinct from each-other.
SAMPLE INPUT:
3 10 8 2
3. Prints a single integer giving the minimum distance Farmer John needs to haul manure in his tractor.
SAMPLE OUTPUT:
3

In this example, the best strategy is to haul the manure from position 3 to position 2, teleport it to position 8, then haul it to position 10. The total distance requiring the tractor is therefore 1 + 2 = 3.