n=int(input())

classship={'B':'BattleShip','C':'Cruiser','D':'Destroyer','F':'Frigate'}
for i in range(n) :
	x=input()
	X=x.upper()
	if X in classship :
		print(classship[X])