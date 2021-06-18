


def check(l):
	for x in l:
		if x[0]<1 or x[0]>10**18 or len(x[1])<1 or len(x[1])>10**5 or not x[1].islower():
			return False
	return True


//hello

if __name__ == '__main__':
	l = []
	T = int(input('enter the vallue of T: '))
	for x in range(0,T):
		N,S = input('enter the vallue of N and S: ').split()
		l.append([int(N),S])
	print(l)

	if (T>=1 and T<=50) and check(l) :
		print('okay to go')
	else:
		print('not okay to go')


