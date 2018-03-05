"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Tuzheng Wei.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('purple', 5)
blue_turtle.speed = 20
henry_pen = rg.SimpleTurtle('turtle')
henry_pen.pen = rg.Pen("red",10)
henry_pen.speed = 5

size = 200

for k in range(5):
    blue_turtle.draw_square(size)
    henry_pen.draw_circle(10)
    henry_pen.left(10)
    blue_turtle.pen_up()
    henry_pen.left(20)
    blue_turtle.right(45)
    blue_turtle.forward(10)
    blue_turtle.left(45)
    blue_turtle.pen_down()


window.close_on_mouse_click()

