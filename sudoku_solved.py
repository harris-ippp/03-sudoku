#!/usr/bin/env python 

import sys

class sudoku():

  def __init__(self, puzzle):

    if type(puzzle) is str:
      self.puzzle = [int(v) for v in puzzle]
    elif type(puzzle) is list:
      # This allows you to leave the mother intact,
      # if you copy the list.
      self.puzzle = [v for v in puzzle]
    else: 
      raise TypeError("Puzzle must be a string or list.")

    # save a copy to check our work later.
    self.initial = [v for v in self.puzzle]

    assert(len(puzzle) == 81)

    # these contain the unassigned numbers for each row, column, and box.
    self.row_unassigned = [set(range(1, 10)) for c in range(9)]
    self.col_unassigned = [set(range(1, 10)) for c in range(9)]
    self.box_unassigned = [set(range(1, 10)) for c in range(9)]

    for cell, val in enumerate(self.puzzle):
      if val: # if it is already assigned.
        # remove it from the possibilities
        self.row_unassigned[cell // 9].remove(val)
        self.col_unassigned[cell %  9].remove(val)
        self.box_unassigned[self.get_box(cell)].remove(val)


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


  def legal(self, verbose = False):

    # check rows, columns, and boxes.
    for i in range(9):
      for v in range(1, 10):
        if [self.puzzle[i*9+x] for x in range(9)].count(v) > 1:
          if verbose:
            print("Bad solution: row {} has multiple {}.".format(i, v))
            print(self)
          return False

        if [self.puzzle[x*9+i] for x in range(9)].count(v) > 1:
          if verbose:
            print("Bad solution: col {} has multiple {}.".format(i, v))
            print(self)
          return False

        # had a block generator... 
        # was nice, but we haven't covered it.
        if [self.puzzle[c] for c in range(81) if self.get_box(c) == i].count(v) > 1:
          if verbose:
            print("Bad solution: box {} has multiple {}.".format(i, v))
            print(self)
          return False

    return True


  def verify_solution(self, verbose = False): # verifying is easy!!

    # If there were no mistakes,
    # this is all you would need.
    if 0 in self.puzzle: 
      if verbose: "Puzzle not complete."
      return False

    for i, s in zip(self.initial, self.puzzle):
      if i and i != s:
        if verbose: print("It is not the same puzzle!!")
        return False

    if not self.legal(verbose): return False
      
    if verbose: print("Looks good!!")
    return True
        

  ## THESE ARE THE MEATY METHODS THAT ACTUALLY DO THINGS...

  def get_box(self, cell): return 3*(cell//27) + (cell%9)//3

  def cell_possibilities(self, i):

    cell =   self.row_unassigned[i // 9] \
           & self.col_unassigned[i %  9] \
           & self.box_unassigned[self.get_box(i)]

    return cell

  def assign_cell(self, cell, value):

    self.puzzle[cell] = value
    self.row_unassigned[cell // 9].remove(value)
    self.col_unassigned[cell %  9].remove(value)
    self.box_unassigned[self.get_box(cell)].remove(value)

  def unassign_cell(self, cell):

    value = self.puzzle[cell]

    self.puzzle[cell] = 0
    self.row_unassigned[cell // 9].add(value)
    self.col_unassigned[cell %  9].add(value)
    self.box_unassigned[self.get_box(cell)].add(value)


  def assign(self):

    assigned = True
    while assigned:
  
      assigned = 0
      for cell, value in enumerate(self.puzzle):

        if value: continue

        possible = self.cell_possibilities(cell)
        if len(possible) == 1:
          assigned += 1
          self.assign_cell(cell, possible.pop())


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


for line in open("sudoku_plane.txt"):

  p = line.strip()
  s = sudoku(p)
  s.assign()
  s.recurse()

  s.verify_solution()

  print(s)


sys.exit()

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



solved, total = 0, 0
with open("sudoku_solved_harder.txt", "w") as out:
  for line in open("sudoku_harder.txt"):

    p = line.strip()
    s = sudoku(p)
    s.assign()
    s.recurse()

    total += 1
    if s.verify_solution(): solved += 1

    out.write(s.__repr__())

print("Hard {}/{} = {:.3f}".format(solved, total, solved/total))

