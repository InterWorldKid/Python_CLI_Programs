"""
Module name: Pattern_Turtle

Contributors:
InterWorldKid


Module description: 
This module has functions that can draw various shapes such as hexagon, circle and square with
different filling and border colors entered by the user as prompted. Those shapes are then put 
in a pattern (order) to display it more than one time on the window screen by using different 
initial positions. Everything was created using the turtle module also the math module to ensure 
symmetry in our shapes. The program was written to provide beatiful geometric visuals, ensuring
symmetry, user-friendly interaction, flexibility, and ease of function usage. This module was 
built upon different user-defined functions and turtle library/modules ready functions.

"""

#import necessary libraries and modules
from turtle import Turtle, Screen
from math import cos, radians

#segment size is the size of a segment from the hexagon, changing this value will also effect
#the other shapes sizes because they all depend on eachother. This variable was made just to ease
#the process of modifying the sizes
segment_size = 100

#this variable will control the spacing between shapes in the pattern
shapes_spacing = 100

# Define the function hexagon that takes a Turtle object 'turta', 
# and two color parameters 'color_hexagon' and 'color_borders'
def hexagon(turta, color_hexagon, color_borders):

    """

    Draws a hexagon using the Turtle object turta, with specified fill and border colors.
    The hexagon is drawn based on the geometric principle that each internal angle of a hexagon 
    is 60 degrees. The turtle starts from the leftmost center point of the hexagon and ends at the
    rightmost center point making it easier to position multiple shapes.

    Parameters:
    turta : The Turtle object used to draw the hexagon.
    color_hexagon : The fill color of the hexagon.
    color_borders : The color of the hexagon's borders.

    """
    #set pen size and color
    turta.pensize(2)
    turta.pencolor(color_borders)

    #start the filling based on the color_hexagon parameter passed value
    turta.begin_fill()

    #draw the hexagon
    turta.left(60)
    turta.fd(segment_size)
    turta.right(60)
    turta.fd(segment_size)
    turta.right(60)
    turta.fd(segment_size)
    turta.right(60)
    turta.fd(segment_size)
    turta.right(60)
    turta.fd(segment_size)
    turta.right(60)
    turta.fd(segment_size)
    turta.right(60)
    turta.fd(segment_size)
    turta.right(60)
    turta.fd(segment_size)
    turta.right(60)
    turta.fd(segment_size)
    turta.left(60)

    #set the fill color and end filling the shape
    turta.fillcolor(color_hexagon)
    turta.end_fill()


def square(turta, color_square, color_borders):

    """

    This function draws a square using the Turtle object turta, with specified fill and border colors.
    The shape is drawn using square half segments to have more control over the shape and ease the 
    positioning process.The square is drawn starting from the center of the leftmost point and ends 
    at the center of the rightmost point. The turtle then lifts up its pen and moves to the right 
    without drawing, preparing for the next shape.

    Parameters:
    turta : The Turtle object used to draw the square.
    color_square : The fill color of the square.
    color_borders : The color of the square's borders.

    """

    #we used square_half_segment to start our square from the middle from the left side of our square
    square_half_segment = segment_size*cos(radians(30)) #to match half of the hexagon hight (basic geometry and trigonometry)

    #set pen size and color
    turta.pensize(2)
    turta.pencolor(color_borders)

    #start the filling based on the color_square parameter passed value
    turta.begin_fill()
    
    #draw the shape
    turta.left(90) #here we turn left by 90 to start with the half segment from the center of the left side
    turta.fd(square_half_segment)
    turta.right(90)
    turta.fd(2*square_half_segment)
    turta.right(90)
    turta.fd(2*square_half_segment)
    turta.right(90)
    turta.fd(2*square_half_segment)
    turta.right(90)
    turta.fd(square_half_segment)
    turta.right(90)

    #set the fill color and end filling the shape
    turta.fillcolor(color_square)
    turta.end_fill() 

    #those lines allow us to stop at the middle of our left side and go to the middle of
    #our right sidethis is just to make distancing shapes easier in the pattern function
    turta.up()
    turta.fd(2*square_half_segment)
    turta.down()


def circle(turta, color_circle, color_borders):

    """
    Draw a circle using the provided turtle object with specified fill and border colors.
    This function basically draws a circle starting from the center of the most left moving
    counter clockwise returning back to its position and then set the turtle on the center of 
    the most right part in order to draw easily providing symmetrical patterns.

    Parameters:
    turtle : The turtle object used for drawing.
    color_circle : The color of the circle's fill.
    color_borders : The color of the circle's border.

    """
    circle_radius = segment_size*cos(radians(30)) #to match half of the hexagon hight (basic geometry and trigonometry)

    #set pen size and color
    turta.pensize(2)
    turta.pencolor(color_borders)
    #set the turtle up position
    turta.right(90)
    #initialize the filling process
    turta.begin_fill()
    #draw the circle
    turta.circle(circle_radius)
    #fill shape
    turta.fillcolor(color_circle)
    #end filling process
    turta.end_fill()
    #set the turtle to point right
    turta.left(90)
    #move the turtle to the center of the right most side
    turta.up()
    turta.fd(2*circle_radius)
    turta.down()

def setPos(turta, x, y):

    """

    The setPos function is responible for shifting the turtle current position to a newly specified
    postion of x and y after completing a full pattern row. In other terms this function determines
    the starting point of a pattern.

    """

    #rise the turtle from the canvas (window)
    turta.up() 
    #go to the specified x and y positions
    turta.goto(x,y) 
    #place back the turtle on the canvas (window)
    turta.down()


def pattern(turta, color_hexagon, color_circle, color_square, color_borders):

    """
    This function draws a pattern of three shapes: a hexagon, a circle, and a square. 
    Each shape has its own fill color and a common border color.

    Parameters:
    turta : A turtle object that will be used to draw the shapes.
    color_hexagon : The fill color for the hexagon.
    color_circle : The fill color for the circle.
    color_square : The fill color for the square.
    color_borders : The color of the borders for all the shapes.

    The function first draws a hexagon using the 'hexagon' function, then moves 
    the turtle forward by a certain spacing before drawing a circle using the 
    'circle' function. It again moves the turtle forward by the same spacing before 
    drawing a square using the 'square' function. The spacing between the shapes is 
    determined by the 'shapes_spacing' variable which is defined at the beginning of the module.
    """

    #draw the hexagon
    hexagon(turta, color_hexagon, color_borders)
    #create a space between the hexagon and the circle
    turta.up()
    turta.fd(shapes_spacing)
    turta.down()
    #draw the circle
    circle(turta, color_circle, color_borders)
    #create a space between the circle and the square
    turta.up()
    turta.fd(shapes_spacing)
    turta.down()
    #draw the square
    square(turta, color_square, color_borders)


def main():

    """
    This function serves as the entry point of the program. It prompts the user to input 
    colors for the hexagon, circle, square, and their borders. Then, it creates a turtle 
    object and a window object, sets the background color of the window, and positions the 
    turtle to draw three patterns on the screen using the 'pattern' function. The purpose 
    of this function is to draw multiple patterns on the screen based on user defined colors. 
    Each pattern consists of a hexagon, a circle, and a square, with distinct fill colors and 
    a common border color. After drawing the patterns, the function waits for the user to click 
    on the window to exit the program.

    """

    color_hexagon = input("Enter the color of hexagon: ") #ask the user for the hexagon color
    color_circle = input("Enter the color of circle: ") #ask the user for the circle color
    color_square = input("Enter the color of square: ") #ask the user for the square color
    color_borders = input("Enter the color of shape borders: ") #ask the user for the borders color

    turta = Turtle() #create a turtle object called turta
    window = Screen() #create a window object called window
    window.bgcolor("#ADD8E6") # set the background color as sky blue using the hexa decimal value #ADD8E6
    window.title("group5-activity1, colorful patterns") #add title to the window

    setPos(turta, -600, 250) #set the starting position for the first pattern
    pattern(turta, color_hexagon, color_circle, color_square, color_borders) #print the first pattern
    setPos(turta, -400, 0) #set the starting position for the second pattern
    pattern(turta, color_hexagon, color_circle, color_square, color_borders) #print the second pattern
    setPos(turta, -200, -250) #set the starting position for the third pattern
    pattern(turta, color_hexagon, color_circle, color_square, color_borders) #print the third pattern

    window.exitonclick()

main()
