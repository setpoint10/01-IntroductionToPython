"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Yu Xin.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
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
#
########################################################################

import rosegraphics as rg
window = rg.TurtleWindow()
first = rg.SimpleTurtle("turtle")
second = rg.SimpleTurtle("square")
size = 360

window.tracer(5)

for k in range(10):
    first.forward(100 - k)
    first.left(size/4 - 2 )
    first.backward(k)
    first.draw_circle(5*k)
    size=size-2

for k in range(10):
    second.draw_square(10*k)
    second.forward(10)
    second.pen_up()
    second.right(90)
    second.pen_down()
    second.backward(k)
    second.left(90)

window.close_on_mouse_click()