um=int(input())
if(num%100==0):
	num=num/100;
	if(num%4==0):
		print("yes")
	else:
		print("no")
else:
	if(num%4==0):
		print("yes")
	else:
		print("no")
