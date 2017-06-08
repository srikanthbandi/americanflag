    
import turtle


### this function is drawn filling colors in the flag ### 

def filling_color(color):
    turtle.begin_fill()
    turtle.color(color)
    turtle.end_fill()    

## this function draws the rectangle ####

def draw_rectangle(height,color):
    turtle.begin_fill()
    turtle.color(color)
    height = float(height)
    length = height *(1.9)
    length = round(length,2)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.begin_fill()
    turtle.color(color)
    turtle.end_fill

### this function draws the canton ###

def draw_canton(height):
    turtle.begin_fill()
    turtle.color("blue")
    x1=0
    y1=0
    height= float(height)
    canton_height = float(height*(7/float(13)))
    canton_width = height*1.9
    canton_width = canton_width * (2/float(5))
    turtle.setpos(x1,y1)
    turtle.right(90)
    turtle.forward(canton_width)
    turtle.right(90)
    turtle.forward(canton_height)
    turtle.right(90)
    turtle.forward(canton_width)
    turtle.right(90)
    turtle.forward(canton_height)
    turtle.right(90)
    filling_color("blue")


#### this function is used to change the arrangment of the turtle ##

def arrangment():
    turtle.pu()
    turtle.left(90)
    turtle.forward(20)
    turtle.pd()


### this function draws the star ##### 

def draw_star(size,color): 

    turtle.speed(100)
    size= float(size)
    turtle.right(90)
    turtle.begin_fill()
    turtle.color(color)
    turtle.down()
    turtle.forward(size)
    turtle.left(144)
    turtle.forward(size)
    turtle.left(144)
    turtle.forward(size)
    turtle.left(144)
    turtle.forward(size)
    turtle.left(144)
    turtle.forward(size)
    turtle.left(144)
    turtle.end_fill()
    #turtle.speed(1)

### this function draws the stars five times ##

def five_stars():
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")

#### this function draws the stars six times ### 

def six_stars():
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")
    arrangment()
    draw_star(8,"white")



####### the below code draws the rectangle by calling the function ######

draw_rectangle(150,"red")

###### after drawing the square the below code brings the turtle to home position #### 

x1=0
y1=0
turtle.setpos(x1,y1)

#### calucuating the stripwidth of the flag ###### 

height = 150
stripwidth = height / float(13)
turtle.speed(100)

x1=0
y1=0-stripwidth

##### the following code draws strips in the rectangular flag ####


for j in range(13):
    if j%2 ==0:

        b=0
        g=0
        r=1
    else:
        r=g=b=1
    turtle.pu()
    turtle.setheading(90)
    turtle.pd()
    turtle.setpos(x1,y1) ### setting the position again and again ## 
    turtle.color(r,g,b)
    length = height *(1.9)
    turtle.begin_fill()
    turtle.forward(stripwidth)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(stripwidth)
    turtle.right(90)
    turtle.forward(length)
    turtle.end_fill()
    y1 -= stripwidth ### bringing the turtle below along the height a stripwidth after each iteration ##

turtle.pu()

### bringing the turtle again to the home ###

x1=0
y1=0
turtle.setposition(x1,y1)
turtle.pd()


turtle.setheading(90)

### drawing the canton by caling the canton function ###

draw_canton(150)

turtle.home()

## drawing stars #####
## setting the turtle position constantly by moving towards x & y axis ###

six_stars()

turtle.pu()
turtle.home()

x1=10
y1=-8
turtle.setposition (x1,y1)

five_stars()

turtle.pu()
turtle.home()

x1=0
y1=-16
turtle.setposition (x1,y1)

six_stars()

turtle.pu()
turtle.home()

x1=10
y1=-24
turtle.setposition (x1,y1)

five_stars()

turtle.pu()
turtle.home()

x1=0
y1=-32
turtle.setposition (x1,y1)

six_stars()

turtle.pu()
turtle.home()

x1=10
y1=-40
turtle.setposition (x1,y1)

five_stars()

turtle.pu()
turtle.home()

x1=0
y1=-48
turtle.setposition (x1,y1)

six_stars()

turtle.pu()
turtle.home()

x1=10
y1=-56
turtle.setposition (x1,y1)
five_stars()

turtle.pu()
turtle.home()

x1=0
y1=-64
turtle.setposition (x1,y1)
six_stars()

turtle.pu()
turtle.home()









