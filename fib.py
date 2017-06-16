def fib(numb):
	a, b = 0, 1
	l = []
	while(a<numb):
		l.append(a)
		a, b = b, a+b
	print (l)

if __name__ == "__main__":
	fib(10)
