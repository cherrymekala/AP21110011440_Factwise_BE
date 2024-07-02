from num2words import num2words

s=""
res=[]

for i in range(1,1001):
	s=num2words(i).replace(" ","").replace("-","")
	res.append(len(s))
print(sum(res))
	
	
