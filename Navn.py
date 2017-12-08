import turtle
t = turtle.Turtle ()
wn = turtle.Screen ()
name = input ("Enter your name: ")
print ("Hello "+name)
if (name == "Frederik"):
	print ("You're cool "+name)
else:
	print ("You're not cool "+name)
figure = input ("Do you want to see a figure? ")
if (figure == "Yes"):
	for i in range(4):
		t.fd(50)
		t.left(90)
else:
	print ("Then I won't show you")

wn.exitonclick()