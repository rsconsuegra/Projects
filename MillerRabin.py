import sys

def MillerRabin(n):
	if (n < 4759123141): 
		semilla= [ 2, 7, 61] 
	elif (n < 341550071728321): 
		semilla= [2, 3, 5, 7, 11, 13, 17]
	else: 
		semilla =  [2, 3, 5, 7, 11, 13, 17, 19, 23]
	d = n - 1
	s=0
	while ((d & 1) == 0):  
		d >>= 1 
		s+=1

	l=1
	for i in range(len(semilla)):
		a   = min(n - 2, semilla[i])
		actual = pown(a, d, n)
		if (actual == 1): 
			continue
		if (actual == n - 1): 
			continue
		print(s)
		for j in range(1,s):
			print(actual,i,j)
			actual = mul(actual, actual, n)
			l=j
			print(j)
			if (actual == n - 1):
				break
		print(l)
		if (l == s):
			return False
	return True

def mul(a,b,mod):
	now = 0
	for i in range(63,-1,-1):
		if (((a >> i) & 1) == 1):
			break
	for i in range(i,-1,-1):
		now <<= 1
		while (now > mod):
		 now -= mod
		if (((a >> i) & 1) == 1):
		 now += b
		while (now > mod):
		 now -= mod
	return now

def pown(a,p,mod):
   if (p == 0):
    return 1
   if (p % 2 == 0):
    return pown(mul(a, a, mod), p / 2, mod)
   return mul(pown(a, p - 1, mod), a, mod)
	

if __name__ == '__main__':
	n = sys.argv[1]
	print(MillerRabin(int(n)))
