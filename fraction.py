class Fraction(object):
	'''Define a fraction type'''
	def __init__(self, num=0, denom=1):
		'''Create a new Fraction with numerator num and denominator demon'''
		self.numerator = num
		if denom != 0:
			self.denominator = denom
		else:
			raise ZeroDivisionError
	def reduce(self):
		gcd = self.findgcd(self.numerator, self.denominator)
		if(gcd):
			self.numerator /= gcd
			self.denominator /= gcd
	def mixed_number(self):
		whole = self.numerator / self.denominator
		modul = self.numerator % self.denominator
		if (modul == 0):
			return whole
		elif (whole == 0):
			return "{0}/{1}".format(modul, self.denominator)
		else:
			return "{0} {1}/{2}".format(whole,modul, self.denominator)
	def __add__(self, f):
		max_value = self.denominator * f.denominator
		temp = Fraction() 
		temp.numerator = max_value/f.denominator * self.numerator + max_value/self.denominator * f.numerator 		
		temp.denominator = max_value 
		return temp
	def __mul__(self, f):
		temp = Fraction()
		temp.numerator = self.numerator * f.numerator		
		temp.denominator = self.denominator * f.denominator
		return temp

	def findgcd(self, x, y):
		gcd = None
		min_number = min(x, y)
		for i in range(min_number, 1, -1):
			if x % i == 0 and y % i == 0:
				gcd = i
				break
		return gcd
	def findlcm(self, x, y):
		lcm = None
		max_number = max(x, y)
		multipy_number = x * y	
		for i in range(max_number, multipy_number + 1):
			if i % x == 0 and i % y == 0:
				lcm = i
				break
		return lcm
	def __repr__(self):
		return "{0}/{1}".format(self.numerator, self.denominator)

class ReducedFraction(Fraction):
	def __init__(self, num = 0, denom = 1):
		Fraction.__init__(self, num, denom)
		self.reduce()
	def __add__(self, f):
		temp = super(ReducedFraction, self).__add__(f)
		temp.reduce()
		return temp
	def __mul__(self, f):
		temp = super(ReducedFraction, self).__mul__(f)
		temp.reduce()
		return temp
