import turtle
t = turtle.Turtle ()
wn = turtle.Screen ()
t.speed(30)
def bsquare (size,line,column):
	if ((((line % 2) == 0) and (column % 2 >0)) or (((line % 2) > 0) and (column % 2 ==0))):
		t.color("black")
		t.begin_fill()
		for i in range(4):
			t.fd(size)
			t.left(90)
		t.end_fill()
		t.color("black")
	else:
		for i in range(4):
			t.fd(size)
			t.left(90)
t.penup()
t.setx(-200)
t.sety(200)
t.pendown()
for line in range(8):
	for column in range(8):
		bsquare(50,line,column)
		t.fd(50)
	if line < 7:
		t.bk(400)
		t.right(90)
		t.fd(50)
		t.left(90)
	else:
		t.penup()	
wn.exitonclick()



