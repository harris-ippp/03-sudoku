#!/usr/bin/env python 

import sys

class sudoku():

  def __init__(self, puzzle):

    self.puzzle = [int(v) for v in puzzle]

    # Save a copy to check our work, later.

    # Initialize the 'unassigned' lists.


  #######
  # CHECKS AND PRINTING

  def __repr__(self):

    return "".join(str(x) for x in self.puzzle) + "\n"


  def __str__(self):

    s = "\n+---+---+---+"
    for b in range(3):
      for r in range(3):
        s += "\n|"
        for c in range(3):
          s += "".join([str(v) for v in self.puzzle[b*27+r*9+c*3:b*27+r*9+c*3+3]]) + "|"
      s += "\n+---+---+---+"
        
    return s
  
  
  def verify_solution(self): # verifying is easy!!
  
    print("Could be!  Let's just say yes!!")
    return True
        

  ## THESE ARE THE MEATY METHODS THAT ACTUALLY DO THINGS...

  def get_box(self, cell): 

    return 0

  # Get the possibilities for the row, column, and box.
  # Their intersection is the possibilities of the cell.
  def cell_possibilities(self, i):

    pass


  # Assign a cell to a value,
  # and remove the possibilities from the row, column, and box.
  def assign_cell(self, cell, value):

    pass


  # Loop over the puzzle repeatedly, 
  # searching for cells where only a single value is possible.
  # In those cases, assign the cell to that single value.
  # For sets, the easiest is s.pop(); for list, it's... the first element!!
  def assign(self):

    pass


  ## Go on... try recursion!  It's fun!!


solved, total = 0, 0
with open("sudoku_solved_easier.txt", "w") as out:
  for line in open("sudoku_easier.txt"):

    p = line.strip()
    s = sudoku(p)
    s.assign()

    total += 1
    if s.verify_solution(): solved += 1

    out.write(s.__repr__())

print("Easy {}/{} = {:.3f}".format(solved, total, solved/total))


