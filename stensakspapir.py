from random import randint
from collections import Counter
global scorelist
scorelist=[]
global commonlist
commonlist=[]
global simgames
simgames=[]
global loops
def randomRPS(rps):
	retur=""
	global score
	if rps=="rock":
		number=1
		if number==random:
			score=1
			retur=retur+"rock, it's a draw!"
		elif number==random+2:
			score=2
			retur=retur+"scissors, you win!"
		else:
			score=-2
			retur=retur+"paper, you lose!"
	elif rps=="paper":
		number=0
		if number==random:
			score=1
			retur=retur+"paper, it's a draw!"
		elif number<random:
			score=2
			retur=retur+"rock, you win!"		
		else:
			score=-2
			retur=retur+"scissors, you lose!"
	elif rps=="scissors":
		number=-1
		if number==random:
			score=1
			retur=retur+"scissors, it's a draw!"
		elif number==random+1:
			score=2
			retur=retur+"paper, you win!"
		else:
			score=-2
			retur=retur+"rock, you lose!"
	scorelist.append(score)
	return(retur)
def cheatRPS(cheatl):
	commonlist=[]
	retur=""
	number=0
	global score
	if cheatl=="rock":
		number=number+1
	if cheatl=="paper":
		number=number+2
	if cheatl=="scissors":
		number=number-1
	li2.append(number)
	c= Counter(commonlist)
	d= c.most_common(1)
	if d[0][0]==1:
		retur=retur+"paper, you lose!"
		score=-2
	if d[0][0]==2:
		retur=retur+"scissors, you lose!"
		score=-2
	if d[0][0]==-1:
		retur=retur+"rock, you lose!"
		score=-2
	scorelist.append(score)
	return (retur)
def cheatRPS2(word3):
	commonlist=[]
	retur=""
	number=0
	global score
	if word3=="rock":
		number=number+1
	if word3=="paper":
		number=number+0
	if word3=="scissors":
		number=number-1
	li2.append(number)
	c= Counter(commonlist)
	d= c.most_common(1)
	if d[0][0]==1:
		retur=retur+"scissors, you win!"
		score=2
	if d[0][0]==0:
		retur=retur+"rock, you win!"
		score=2
	if d[0][0]==-1:
		retur=retur+"paper, you win!"
		score=2
	scorelist.append(score)
	return (retur)
def Sim ():
	import random
	global simgames
	simgames=[]
	for i in range(loops):
		result=""
		randomactions=["scissors","paper","rock"]
		playera= random.choice(randomactions)
		playerb= random.choice(randomactions)
		if playera==playerb:
			result="draw"
		elif playera=="scissors" and playerb=="rock":
			result="lose"
		elif playera=="rock" and playerb=="scissors":
			result="win"
		elif playera=="paper" and playerb=="scissors":	
			result="lose"
		elif playera=="paper" and playerb=="rock":
			result="win"
		elif playera=="scissors" and playerb=="paper":
			result="win"
		elif playera=="rock" and playerb=="paper":
			result="lose"
		result=result+" "+playera+" "+playerb
		simgames.append(result)
	return 
def AIRPS(human):
	global loops
	wingames=[]
	retur=""
	global score
	for i in range(loops):
		temp=str(simgames[i])
		if temp[0:4]=="lose" and temp[5:5+len(human)]==human:
			wingames.append(temp[6+len(human):len(temp)])
	if human==wingames[0]:
		retur=retur+wingames[0]+", "+"it's a draw!"
		score=1
	elif human=="scissors" and wingames[0]=="rock":
		retur=retur+wingames[0]+", "+"you lose!"
		score=-2
	elif human=="rock" and wingames[0]=="scissors":
		retur=retur+wingames[0]+", "+"you win!"
		score=2
	elif human=="paper" and wingames[0]=="scissors":
		retur=retur+wingames[0]+", "+"you lose!"
		score=-2
	elif human=="paper" and wingames[0]=="rock":
		retur=retur+wingames[0]+", "+"you win!"
		score=2
	elif human=="scissors" and wingames[0]=="paper":
		retur=retur+wingames[0]+", "+"you win!"
		score=2
	elif human=="rock" and wingames[0]=="paper":
		retur=retur+wingames[0]+", "+"you lose!"
		score=-2
	scorelist.append(score)
	return (retur)		
start=input("Mode[Random,CheatL, CheatW, SIM or AI]: ")
count= 0
print ("[+2 Win] [+1 Draw] [-2 Lose] Commands: 'stop' 'score' 'mode'")
while count==0:
	if start=="random":
		rps=input ("RPS: ")
		if rps=="mode":
			start=input("Mode: ")
		elif rps=="score":
			print ("Your score is "+ str(sum(scorelist)))
		elif rps=="stop":
			count=count+1
			print ("Your final score is "+str(sum(scorelist)))
		else:
			random= randint(-1, 1)
			print(randomRPS(rps))
	if start=="cheatl":
		cheatl=input ("RPS: ")
		if cheatl=="mode":
			start=input("Mode: ")
		if cheatl=="score":
			print ("Your score is "+ str(sum(scorelist)))
		elif cheatl=="stop":
			count=count+1
			print ("Your final score is "+str(sum(scorelist)))
		else:
			print(cheatRPS(cheatl))
	if start=="cheatw":
		cheatw=input ("RPS: ")
		if cheatw=="mode":
			start=input("Mode: ")
		if cheatw=="score":
			print ("Your score is "+ str(sum(scorelist)))
		elif cheatw=="stop":
			count=count+1
			print ("Your final score is "+str(sum(scorelist)))
		else:
			print(cheatRPS2(cheatw))
	if start=="ai":
		human=input ("RPS: ")
		if human=="mode":
			start=input("Mode: ")
		if human=="score":
			print ("Your score is "+ str(sum(scorelist)))
		elif human=="stop":
			count=count+1
			print ("Your final score is "+str(sum(scorelist)))
		else:
			print(AIRPS(human))
	if start=="sim":
		loops=int(input ("Enter a value: "))
		Sim()
		start=input("Enter mode: ")
