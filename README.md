# tl;dr: Solve Sudoku

# Solving the Sudoku Issue

We've all seen the crumpled magazine pages, lacerated by markings and desperate unmarkings.  Many of us have watched family members succumb to this "pastime" before abandoning hope when time runs out on their "flight."  Some of you may even have experimented with this 9 by 9 matrix, this cage, this trap.

Yet Sudoku is very much a solvable problem.  In this mission, you will endeavor to rid the world of this menace, providing humanity with a definitive solution for the "Sudoku Issue."  In so doing, we will improve workers' productivity, unburden the elderly, remove excuses for avoiding human contact on long flights, and save trees.  The cause is great; our resolve is strong!

You will work in teams of up to three (marked on your homework), and submit to a common repository.  If you decide to go it alone, you may -- the cost is just that you have to do all of the work.  I encourage you to use Piazza to find partners if need be.

## The Sudoku Problem

At stake are 81 squares arranged in a 9×9 grid.  The conceit is that (a) each row must contain the numbers 1 through 9, (b) so too must each column, and lastly (c) likewise for each of the 9 3×3 blocks.  The challenge is to identify numbers that satisfy (a-c) given a partially completed puzzle.  I have a collected a number of puzzles -- some easier (`sudoku_easier.txt`) and others more fiendish (`sudoku_harder.txt`) -- as test cases for your algorithms.

## Implementing the Problem

Each puzzle consists of a list of 81 single-digit numbers (0-9), where 0 represents unassigned values.
It will be useful for you to maintain a list or a `set` (like a list, but unique) 
of the unassigned digits in each row, column, and box.

(Alternatively, you could retain a list of the remaining possibilities in every square;
  this would work just as well, but below I give some hints for the unassigned row/col/box strategy.)

## Not All Sudoku Are Created Equal

The first item of business is to assign values to initially empty squares.
You can do this by considering the unassigned possibilites for the row, column, and box corresponding to that cell.
If there is a single value that is possible in all three (that lies in the _intersection of the sets_), 
    assign that cell to that value.
For example, if a cell's row does has not assigned possitions for `{2, 4, 6, 7}`,
    the column has not assigned values for `{4, 5, 6, 7}`,
    the box has assigned values for all but `{2, 7, 8, 9}`
    then the only possible value fo the cell is `7`.
On the other hand, if there are multiple possible values, hold tight for a moment -- wait until there's only one.
By following this sequence repeatedly (`while`),
    looping (`for`) over all the cells in the puzzle (`for`),
    you can progressively fill in all of the cells.

This iterative procedure is enough to solve all of the "easier" puzzles.

**The solution format will be files containing the same puzzles as `sudoku_easier.txt` and `sudoku_harder.txt`,
  in the same order and format (81-digit strings), but solved.**

Take some time to discuss _how_ to solve the problem first, with your group.
It will be much easier to write, if you know what you want.

<details>
<summary>Suggested methods.</summary>

You may solve this any way you like, but here are some suggested functions to implement.
* `__init__()`: Make a class.  In the `__init__()` function, accept a string and turn it into an 81-item list.
   This will be easier to manipulate.  You could also make lists of the unassigned possibilities in each row, column, and box.
   Start with sets or lists containing 1-9, and `remove()` the value that are already assigned.
   This could also live in another method that you call at this point.
* `__str__()`: Defining a nice `__str__()` method will allow you to just call `print(puzzle)` 
   or `print(self)` from with the class.  This will probably help you to debug.
* `__repr__()`: Use this to write 81-digit strings back to your solutions output file, 
   in the same format as you read them in.
* `get_box()`: Given the cell index, it's pretty easy to figure out the row (`cell // 9`) 
   or column (`cell % 9`).  The box is a little trickier.  Write the method once, check it carefully, 
   and call it when you need it.
* `assign_cell()`: Set a cell of the puzzle from 0 to a value, and remove it from the unassigned lists or sets
  for its row, column, and block.
* `assign()`: Call `assign_cell()` or similar in two nested loops: an outer loop over the entire puzzle 
  (terminating when you can't make any more assignments), and an inner `for` loop over all of the cells.
  Use `continue` to skip the already-assigned values...
* `verify_solution()`: Write a method to check your solution.  Try to check three conditions:
   1. The initial values should all be there.  To check this, you'd need to somehow save a copy
      of the initial state of the puzzle, before you started working on it.
   2. There should be no zeroes left in the puzzle.
   3. Every row, column, and box should have exactly one of the digits 1-9.
</details>

## Recursion or Other Strategies

As a next step, you could consider assigning a value to a cell
   if it is the only cell in its column, row, or box to have that possibility.

There then follows a long list of tortured "coping mechanisms" for this addiction; see [Sudoku Dragon](http://www.sudokudragon.com/sudokustrategy.htm).  You _may_ use any of these if you want, but at this juncture I would make a suggestion: try random assignment.

**Your goal is to solve more than 40% of the harder puzzles.  The recursion strategy will work 100% of the time.**

### Random Assignment and Recursion

At this point, you have a largely solved puzzle, with a certain number of possibilities in each box.
Proceed to the first unassigned box, 
    assign it to one of its possibilities,
    and remove that possibility from its row, column, and box.
Continue on to the next empty/non-assigned cell, and assign _it_ to one of _its_ possibilities, and so forth

Repeatedly calling a method, deeper and deeper within itself, is called _recursion_; we'll call this method `recurse()`.
The first time that you find a box without any possibilities, you've found a contradiction.
So then `recurse()` has to backtrack -- _unassigning_ the value
  (and adding back in the possibility for the row, column, and box).
You can signal whether to back-track or continue onwards by returning `False` or `True`.

<details>
<summary>More hints.</summary>

* `unassign_cell()`: This is simply the 'inverse' of the `assign_cell()` function above.
  You'll need to call it when recursion on a single option fails.
* `recurse()`: This function needs to do three things in a loop: 
  assign one of the test cases, try going deeper, and returning false
  if there are no possibilities in an empty cell.
  
  ```
  def recurse(self):
  
    # Loop over all the cells.
    for cell in range(81):
  
      # if it's assigned, keep going
      if self.puzzle[cell]: continue
  
      for poss in self.cell_possibilities(cell):
  
        # Assign the cell
        self.assign_cell(cell, poss)
  
        # continue deeper in the recursion.
        if self.recurse(): return True
  
        # If this choice failed -- 
        # at some point there were no options,
        # then we have a contradiction.
        # Unassign the cell and revert the 
        # possibilities, and try the next one.
        self.unassign_cell(cell)
  
      # When there is no possible value,
      # we have a contradiction, 
      # and use unassign to back up.
      return False
  
    # until we fall off the end.
    return self.verify_solution()
  ```

</details>


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

Consider their solutions if you like, but the final code must be yours. 

The solutions are due October 19 at 1:30am.

### Additional Final Words

Good luck!  
