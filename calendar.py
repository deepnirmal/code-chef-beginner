n=int(input())
days={0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}
for _ in range(n) :
	year=int(input())
	ans=1
	if year>2001: 
		for i in range(2001,year) :
			if (i%4==0 and i%100!=0) or i%400==0 :
				ans+=2
			else:
				ans+=1	



	else: 
			for i in range(1900,year) :
				if (i%4==0 and i%100!=0 )or i%400==0 :
					ans+=2
				else:
					ans+=1	
			
	ans=ans%7 				
	print(days[ans])
	
