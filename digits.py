#Ashab Naveed 
#Computing Science 10
#Logo
#Henry Wise Wood High School
#2021-22 Semester 1
#November 18th, 2021

def draw_line (t,r): #defines the stamp function and moves forwards to stamp at the next line
  for i in range(r): #follows the second parameter to set how many stamps it does
    t.stamp()
    t.forward(16)

def line (t, r): #the inverse of draw_line (backwards)
  for i in range(r):
    t.stamp()
    t.backward(16)

def draw_zero(t): #moves forwards 16 and uses a loop to draw the circle of the zero
  t.forward(16)
  for i in range(2):
    draw_line(t, 2)
    t.right(90)
    draw_line(t,4)
    t.right(90)
  t.forward(48)

def draw_one(t): #moves to the last line and draws the one, moving back up to the top right
  t.forward(48)
  t.right(90)
  draw_line(t, 5)
  t.right(180)
  t.forward(16 * 5)
  t.right(90)
  t.forward(16)

def draw_two(t): #goes forward 1 block and draws 2 moving back to the top right
  t.forward(16)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(270)
  draw_line(t, 2)
  t.right(270)
  draw_line(t, 3)
  t.left(90)
  t.forward(64)
  t.right(90)

def draw_three(t):#draws 3 starting one block forwards
  t.forward(16)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(180)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 3)
  t.right(90)
  t.forward(64)
  t.right(90)
  t.forward(64)

def draw_four(t): #draws 4 going one block forwards
  t.forward(16)
  t.right(90)
  draw_line(t, 2)
  t.left(90)
  draw_line(t, 2)
  t.left(90)
  draw_line(t, 2)
  t.left(180)
  draw_line(t, 5)
  t.right(180)
  t.forward(80)
  t.right(90)
  t.forward(16)

def draw_five(t): #draws 5 going 3 blocks forwards and moving backwards, utilizing the line function from beforehand
  t.forward(48)
  line(t, 2)
  t.left(90)
  line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 3)
  t.right(90)
  t.forward(64)
  t.right(90)
  t.forward(64)

def draw_six(t): #draws 6 from the last block moving backwards
  t.forward(48)
  line(t, 2)
  t.left(90)
  line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 4)
  t.right(90)
  t.forward(48)

def draw_seven(t): #draws 7 moving forwards one block
  t.forward(16)
  draw_line(t, 2)
  t.right(90)
  draw_line(t, 5)
  t.right(180)
  t.forward(80)
  t.right(90)
  t.forward(16)

def draw_eight(t): #fills one block that was missing from 6 and calls the function draw_six to fill in the rest of the box
  t.forward(48)
  t.right(90)
  draw_line(t, 2)
  t.left(180)
  draw_line(t, 2)
  t.right(90)
  t.backward(48)
  return draw_six(t)
  
def draw_nine(t): #fills in the missing block from 3 and then calls the function to fill in the rest of the box
  t.forward(16)
  t.right(90)
  draw_line(t, 2)
  t.right(180)
  t.forward(32)
  t.right(90)
  t.backward(16)
  return draw_three(t)
