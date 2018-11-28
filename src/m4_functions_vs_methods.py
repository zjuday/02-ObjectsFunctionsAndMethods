"""
Demonstrates using (calling) FUNCTIONS and using (calling) METHODS:
  -- what is similar, and
  -- how they differ.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zachary Juday.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# DONE: 2.
#   With your instructor, READ the file   methods_vs_functions.txt
#   in this project, ASKING QUESTIONS as needed to understand its contents.
#   After you have done so, mark this _TODO_ as DONE
#   and continue to the next _TODO_.
#
###############################################################################


import rosegraphics as rg


def main():
    """
    Makes a TurtleWindow, calls the other functions in this module
    to test and/or demonstrate them, and waits for the user to click
    anywhere in the window to close it.
    """
    window = rg.TurtleWindow()

    run_example()
    try_methods()
    try_functions()
    try_methods_and_functions()

    window.close_on_mouse_click()


def run_example():
    """ An example of CALLING functions defined below. """
    jump_and_move_turtle(100, 50, 200, -100)

    turtle = rg.SimpleTurtle('square')
    turtle.speed = 30
    draw_many_squares(turtle, 3, 75, 15)


def jump_and_move_turtle(x1, y1, x2, y2):
    """
    Constructs a thick, slow, magenta SimpleTurtle.
    Jumps that SimpleTurtle (without drawing) to (x1,  y1),
    then moves that Turtle (while drawing) to (x2, y2).
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO-DO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the other problems.
    # -------------------------------------------------------------------------
    jumper = rg.SimpleTurtle()
    jumper.pen = rg.Pen('magenta', 20)
    jumper.speed = 3

    jumper.pen_up()
    jumper.go_to(rg.Point(x1, y1))

    jumper.pen_down()
    jumper.go_to(rg.Point(x2, y2))


def draw_many_squares(my_turtle, number_of_squares, size, twist):
    """
    Makes the given   SimpleTurtle   object draw:
      -- many squares (how many? answer: NUMBER_OF_SQUARES)
    where each square:
      -- has the same size (what size? answer: SIZE)
    and each square is:
      -- "twisted" a bit from the previous one (how much? TWIST degrees)

    NOTE: The 3 lines below that begin with   :type   are called
    "type hints".  They make the "dot" trick work more effectively.
    We will include them in function specifications routinely.
      :type  my_turtle:          rg.SimpleTurtle
      :type  number_of_squares:  int
      :type  size:               int
      :type  twist:              int
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO-DO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the other problems.
    # -------------------------------------------------------------------------
    for _ in range(number_of_squares):
        my_turtle.draw_square(size)
        my_turtle.left(twist)

###############################################################################
# DONE: 3.
#   There are four FUNCTIONS defined ABOVE this:
#     main
#     run_example
#     jump_and_move_turtle
#     draw_many_squares
#
#   1. RUN this program.
#   2. TRACE the code, identifying what code causes what to be drawn.
#   3. READ the specifications for the following functions:
#        jump_and_move_turtle
#        draw_many_squares
#
#   IMPORTANT: Keep those two functions (and what they do) in mind,
#   since you will use them in the:
#     try_functions
#     try_methods_and_functions
#   exercises below.
#
#   Once you believe that you completely understand what the functions:
#        jump_and_move_turtle
#        draw_many_squares
#   do, mark this _TODO_ as DONE and continue to the next _TODO_.
#
###############################################################################


def try_methods():
    """
    Constructs a SimpleTurtle and sets its   pen   to a new rg.Pen
    that is 'brown' with thickness 5.
    Then makes the SimpleTurtle move as follows (in the order listed):
      -- forward   150 units
      -- left       90 degrees
      -- forward    50 units
      -- backward  100 units
    """
    ###########################################################################
    # DONE: 4. Implement and test this function, per its doc-string above.
    #   The testing code (in main) is already written for you.
    ###########################################################################
    t1 = rg.SimpleTurtle('classic')
    t1.pen = rg.Pen('brown', 5)
    t1.forward(150)
    t1.left(90)
    t1.forward(50)
    t1.backward(100)

###############################################################################
# IMPORTANT: Read the NOTE below before you try to implement the next function!
###############################################################################
def try_functions():
    """
    Causes several SimpleTurtles to do the following:
     -- One jumps to (200, 100), then moves (while drawing) to (300, 30)
     -- One jumps to (100, 200), then moves (while drawing) to (0, 0)
     -- One jumps to (-50, 50), then moves (while drawing) to (100, 100)
    """
    ###########################################################################
    # DONE: 5. Implement and test this function, per its doc-string above.
    #   The testing code (in main) is already written for you.
    #
    #    NOTE: This function requires
    #      ** exactly 3 lines **
    #    If you think it needs more, ** ASK FOR HELP. **
    #    HINT: see   jump_and_move_turtle   above.
    ###########################################################################
    jump_and_move_turtle(200,100,300,30)
    jump_and_move_turtle(100,200,0,0)
    jump_and_move_turtle(-50,50,100,100)
###############################################################################
# IMPORTANT: Read the NOTE below before you try to implement the next function!
###############################################################################
def try_methods_and_functions():
    """
    Constructs a SimpleTurtle and sets its   pen  to a new rg.Pen
    that is 'blue' with thickness 5.

    Then makes the SimpleTurtle do the following (in the order listed):

      1. Go  backward  150 units.

      2. Change its speed to 1 (slowest).
         Draw 2 squares whose size (width and height) are 100,
         each "twisted" from the previous by 30 degrees.

      3. Change its speed to 5 (faster).
         Change its Pen's color to 'red'.
         Draw 10 squares whose size (width and height) are 50,
         each "twisted" from the previous by 15 degrees.

      4. Change its speed to 100 (about the fastest possible).
         Change its Pen's thickness to 35.
         Draw 8 squares whose size (width and height) are 300,
         each "twisted" from the previous by 60 degrees.

      5. Change its Pen to be a NEW Pen whose color is 'black'
         and whose thickness is 3.

      6. Go backward  200 units.

      7. Draw a CIRCLE whose radius is 30.

      8. Draw a SQUARE whose sides are each of length 50.
    """
    ###########################################################################
    # DONE: 6. Implement and test this function, per its doc-string above.
    #   The testing code (in main) is already written for you.
    #
    #   NOTE: This function should ** CALL ** the
    #     draw_many_squares
    #   function defined above.  If you don't see why, ** ASK FOR HELP. **
    ###########################################################################
    pinky = rg.SimpleTurtle('classic')
    pinky.pen = rg.Pen('blue', 5)
    pinky.backward(150)
    pinky.speed = 1
    draw_many_squares(pinky,2,100,30)
    pinky.speed = 5
    pinky.pen = rg.Pen('red', 5)
    draw_many_squares(pinky,10,50,15)
    pinky.speed = 100
    pinky.pen = rg.Pen('red', 35)
    draw_many_squares(pinky,8,300,60)
    pinky.pen = rg.Pen('black', 3)
    pinky.backward(200)
    pinky.draw_circle(30)
    draw_many_squares(pinky,1,50,0)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

main()
