# tl;dr Solve Sudoku

# Solving the Sudoku Issue

We've all seen the crumpled magazine pages, lacerated by markings and desperate unmarkings.  Many of us have watched family members succumb to this "pastime" before abandoning hope when time runs out on their "flight."  Some of you may even have experimented with this 9 by 9 matrix, this cage, this trap.

Yet Sudoku is very much a solvable problem.  In this mission, you will endeavor to rid the world of this menace, providing it with a definitive solution for the "Sudoku Issue."  In so doing, we will improve workers' productivity, unburden the elderly, remove excuses for human contact on long flights, and save trees.  The cause is great; our resolve is strong!

You will work in teams of up to three (marked on your homework), and submit to a common repository.  If you decide to go it alone, you may -- the cost is just that you have to do all of the work.  I encourage you to use Piazza to find partners if need be.

## The Sudoku Problem

At stake is are 81 squares arranged in a 9×9 grid.  The conceit is that (a) each row must contain the numbers 1 through 9, (b) each column must as well, and (c) each of the 9 3×3 blocks (see drawing) must as well.  The challenge is to identify numbers that satisfy (a-c) given a partially completed puzzle.  I have a collected a number of puzzles -- some easier (`sudoku_easier.txt`) and others more fiendish (`sudoku_harder.txt`) -- as test cases for your algorithms.

## Implementing the Problem

Each puzzle consists of a list of 81 single-digit numbers (0-9), where 0 represents unassigned values.  It will be useful for you also to retain a list of the remaining possibilities in every square.

## Not All Sudoku Are Created Alike

The first item of business is to eliminate the possibilities from each unassigned squares, based on the contents of their respective rows, columns, and blocks.  When a cell has only a single possibility left, assign it that value.  Simply following this procedure repeatedly should be enough to solve all of the "easier" puzzles.

## Recursion or Other Strategies

As a next step, you may assign a cell a value, if it is the only cell in its row, column, or box to contain that value.  Adding in this additional step, you should be able to solve about half of the harder puzzles.

There then follows a long list of repulsive "coping mechanisms" for this addiction; see [Sudoku Dragon](http://www.sudokudragon.com/sudokustrategy.htm).  You _may_ use any of these if you want, but at this juncture I would make a suggestion: try random assignment.

**Your goal is to solve more than 90% of the harder puzzles.  The recursion strategy will work 100% of the time.**

### Random Assignment and Recursion

At this point, you have a largely solved puzzle, with a certain number of possibilities in each box.  When you can't get any further on the possibilities above, create a new puzzle, assigning the box to one of its possibilities, and trying to solve that one.  If that works (you get a solution), great.  If it doesn't, try assigning another of the possibilities.  If that works great.  If you need to try assignment on another box, do so!

## A Final Word 

Others have come before you, proposing solutions to this problem.  There are many solutions on the interwebs that did not ultimately gain widespread adoption, because their proponents did not have the tenacity and policy chops of students at the Harris School of Public Policy.  For instance, you could find [this](http://blog.davidsingleton.org/sudoku/) unreadable mess

```
def r(a):
 i=a.find('0')
 if i<0:print a
 [m in[(i-j)%9*(i/9^j/9)*(i/27^j/27|i%9/3^j%9/3)or a[j]for
j in range(81)]or r(a[:i]+m+a[i+1:])for m in`14**7*9`]
r(raw_input())
```

Consider their solutions if you like, but the final code must be yours.  Given the skeleton, I'm asking for a somewhat specific format.  

The solutions are due October 19 at 1:30am.

### Additional Final Words

Good luck!  
