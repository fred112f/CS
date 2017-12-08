import turtle
t = turtle.Turtle ()
wn = turtle.Screen ()
t.speed(30)
def bsquare (size):
	t.begin_fill()
	for i in range (4):
		t.fd(size)
		t.left(90)
	t.end_fill()
t.penup()
t.setx(-200)
t.sety(200)
t.pendown()
wn.colormode(255)
for j in range (1):
	for a in range (8):
		t.color(30*a,0,0)
		bsquare(50)
		t.fd(50)
wn.exitonclick()
