'''
Save Beta Rabbit
================

Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of 
each room (except for the top left room) is a hungry zombie. In order to be freed, and to avoid being 
eaten, Beta Rabbit must move through this grid and feed the zombies.


Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to 
the room above, below, left, and right. There is no door in cases where there is no room in that 
direction. However, the doors are locked in such a way that Beta Rabbit can only ever move to the 
room below or to the right. Once Beta Rabbit enters a room, the zombie immediately starts crawling 
towards him, and he must feed the zombie until it is full to ward it off. Thankfully, Beta Rabbit 
took a class about zombies and knows how many units of food each zombie needs be full.


To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry 
zombie) and have used most of the limited food he has. He decides to take the path through the grid 
such that he ends up with as little food as possible at the end.


Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at 
the end, given that he takes a route using up as much food as possible without him being eaten, and 
ends at the bottom right room. If there does not exist a route in which Beta Rabbit will not be 
eaten, then return -1.


food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 
200.

grid will be a list of N elements. Each element of grid will itself be a list of N integers each, 
denoting a single row of N rooms. The first element of grid will be the list denoting the top row,
 the second element will be the list denoting second row from the top, and so on until the last 
element, which is the list denoting the bottom row. In the list denoting a single row, the first 
element will be the amount of food the zombie in the left-most room in that row needs, the second 
element will be the amount the zombie in the room to its immediate right needs and so on. The top 
left room will always contain the integer 0, to indicate that there is no zombie there.


The number of rows N will not exceed 20, and the amount of food each zombie requires will be a 
positive integer not exceeding 10.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) food = 7
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 0

Inputs:
    (int) food = 12
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 1

Use verify [file] to test your solution and see how it does. When you are finished editing your code, 
use submit [file] to submit your answer. If your solution passes the test cases, it will be removed 
from your home folder.
'''

def answer(food, grid):
    def memo(f):
        """
        Memoization wrapper saves the result each time the function is called.
        """
        memory = {}
        def helper(*args):
            if args not in memory:            
                memory[args] = f(*args)
            return memory[args]
        return helper
    
    @memo
    def food_left(food_now, x, y):
        """
        Recursive function.
        If out of bounds or no food left, returns more food (to eliminate path).
        Elif in the top row, return the remaining food.
        Else call self to compare the cell to the left and the cell above
        """
        food_now -= grid[y][x]
        if x < 0 or y < 0 or food_now < 0:
            return food + 1
        elif x == y == 0:
            return food_now
        else:
            return min(food_left(food_now, x - 1, y), food_left(food_now, x, y - 1))
    
    #Start at the bottom right corner, if no path available return -1
    food_after_maze = food_left(food, len(grid) - 1, len(grid) - 1)
    return food_after_maze if food_after_maze <= food else -1
    
print "answer: %s" % (answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]]))

print "answer: %s" % (answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]]))