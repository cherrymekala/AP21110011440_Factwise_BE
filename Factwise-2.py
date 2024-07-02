cardPoints=eval(input())
k=int(input())
n=len(cardPoints)
current=sum(cardPoints[:k])
maxi=current
for i in range(1,k+1):
	current=current-cardPoints[k-i]+cardPoints[-i]
	maxi=max(maxi,current)
print(maxi)
