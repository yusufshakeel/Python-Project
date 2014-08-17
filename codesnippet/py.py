t=input()
while t:
	t-=1
	nk=map(int,raw_input().split(' '))
	n=nk[0]
	k=nk[1]
	p=map(int,raw_input().split(' '))
	for j in range(0,k):
		df=0
		for i in range(0,n-1):
			if p[i]<p[i+1]:
				p.pop(i)
				df=1
                break;
		if df==0:
			p.pop(n-1)
	print ''.join([str(item)+" " for item in p])
