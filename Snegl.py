import turtle
t = turtle.Turtle ()
wn = turtle.Screen ()
t.speed(10)
def snail (size):
	for i in range (20):
		t.fd(size*i)
		t.left(90)
snail(10)
wn.exitonclick()