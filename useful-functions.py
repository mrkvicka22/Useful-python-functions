import math

def divisorsOf(n):
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
	c = 3
	while c <= math.floor(math.sqrt(n)) and math.floor(math.sqrt(n)) % 2 != 0 :
		if math.floor(math.sqrt(n)) % c == 0:
			return False
		else:
			c = c + 2
	return True

def countDigits(n):
	digitsNumber = [int(i) for i in str(n)]
	return len(digitsNumber)

def factorial(n):
  result = 1
  if n <= 0:
    return "you cannot make factorial of negative number";
  else:
    while n > 1:
      result = result * n
      n = n - 1
    return result;
