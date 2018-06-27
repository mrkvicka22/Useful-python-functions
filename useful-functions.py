import math

def d(n):
	c = 1
	sumDiv = 0
	while c < n:
		if n % c == 0:
			sumDiv = sumDiv + c
		else:
			pass
		c = c + 1
	return sumDiv

def D(n):
	c = 1
	divisorsCount = 0
	while c <= math.floor(math.sqrt(n)):
		if n % c == 0:
			if c == math.sqrt(n) and n % c == 0:
				divisorsCount = divisorsCount + 1
				c = c + 1
			else:
				divisorsCount = divisorsCount + 2
				c = c + 1
		else:
			c = c + 1
	return divisorsCount

def isPrime(n):
	c = 2
	while c <= math.floor(math.sqrt(n)):
		if n % c == 0:
			return False
		else:
			c = c + 1
	return True

def countDigits(n):
	digitsNumber = [int(i) for i in str(n)]
	return len(digitsNumber)
