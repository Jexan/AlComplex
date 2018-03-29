import math as m
import cmath as cm

# Settings

def use_j(option):
	Complex.symbol = 'j' if option else 'i'

# Transforms a Real Number to Complex

def real_to_complex(z):
	if not isinstance(z, Complex):
		return Complex(z,0)
	else:
		return z

# Basic Properties

def conjugate(z):
	z = real_to_complex(z)

	return Complex(z.real, -z.imag)

def module(z):
	return m.sqrt(z.real**2+z.imag**2)

def phase(z):
	return m.atan2(z.imag,z.real)

def real(z):
	if isinstance(z, Real):
		return z
	return z.real

def imaginary(z):
	if isinstance(z, Real):
		return 0
	return z.imag

# -------- Singly valued Functions --------

def exp(z):
	z = real_to_complex(z)

	return Complex.python_j(cm.exp(z.py_complex()))

def Ln(z):
	z = real_to_complex(z)

	return Complex.python_j(cm.log(z.py_complex()))

def inverse(z):
	z = real_to_complex(z)

	return z**-1

def sqrt(z):
	z = real_to_complex(z)

	return Complex.python_j(cm.sqrt(z.py_complex()))

# ------- Trigonometric -----------

def sin(z):
	z = real_to_complex(z)

	return Complex.python_j(cm.sin(z.py_complex()))

def cos(z):
	z = real_to_complex(z)

	return Complex.python_j(cm.cos(z.py_complex()))

def tan(z):
	z = real_to_complex(z)

	return Complex.python_j(cm.tan(z.py_complex()))

def sec(z):
	return cos(z)**-1

def csc(z):
	return sin(z)**-1

def cot(z):
	return tan(z)**-1

# --------- Hyperbolic Functions -----

def sinh(z):
	z = real_to_complex(z)

	return (exp(z) - exp(-z))/2

def cosh(z):
	z = real_to_complex(z)

	return (exp(z) + exp(-z))/2

def tanh(z):
	z = real_to_complex(z)
	e = exp(2*z)

	return -i*(e-1)/(e+1)

def sech(z):
	return 1/cosh(z)

def csch(z):
	return 1/sinh(z)

def coth(z):
	return 1/tanh(z)

# ----- Inverse Functions -----

def asin(z):
	z = real_to_complex(z)

	return -i*Ln(i*z-sqrt(1-z**2))

def acos(z):
	z = real_to_complex(z)

	return -i*Ln(z+i*sqrt(1-z**2))

def atan(z):
	z = real_to_complex(z)

	return i/2*Ln(i+z/(1-z))

def asinh(z):
	z = real_to_complex(z)
	return Ln(z+sqrt(z**2+1))

def acosh(z):
	z = real_to_complex(z)
	return Ln(z+sqrt(z**2-1))

def atanh(z):
	z = real_to_complex(z)
	return .5*Ln(i+z/(1-z))

# Multiple Valued Functions

def roots(z, n, include_self=False):
	if not isinstance(n, int) or n <= 0:
		raise TypeError('The n must be an integer greater than zero.')

	z = real_to_complex(z)

	polar = z.polar_coord()
	magnitude = polar[0]**(1/n)
	arg = polar[1]/n

	growth = pi2/n

	for k in range(n):
		yield Complex.polar(magnitude, arg+k*growth)
	
	if include_self: yield z

def ln_values(z, n_start=0, n_finish=False, decreacing=False):
	if (not isinstance(n_start, int) or 
			(n_finish is not False and not isinstance(n_start, int))):
			raise TypeError('The starting and finishing numbers must be integers.')

	z = real_to_complex(z)

	real = m.log(z.abs())
	arg = z.phase()

	counter = n_start

	if n_finish is not False:
		step = 1 if (n_start <= n_finish) else -1
	else:
		step = -1 if decreacing else 1 
		n_finish = [1] # Since False == 0, any range that contains 0 fails unless we do this

	while counter != n_finish:
		yield Complex(real, arg + pi2*counter)	
		counter += step

def ln_n_branch(z,n):
	if not isinstance(n, int):
		raise TypeError('The n must be an integer.')

	return Ln(z) + pi2*n*i	

class Complex():
	symbol = 'i'
	precission = 1e-14

	def polar(r, arg):
		return Complex(round(r*m.cos(arg), 15), round(r*m.sin(arg),15))

	def python_j(r):
		return Complex(r.real, r.imag)

	def py_complex(self):
		return self.real + self.imag*1.j

	def to_float(self):
		if self.imag == 0:
			return float(self.real)
		else:
			raise TypeError('Cannot convert to float; imaginary part is not zero.')

	def to_int(self):
		if self.imag == 0:
			return int(self.real)
		else:
			raise TypeError('Cannot convert to int; imaginary part is not zero.')

	def abs(self):
		return module(self)

	def module(self):
		return module(self)

	def magnitude(self):
		return module(self)

	def phase(self):
		return phase(self)

	def arg(self):
		return phase(self)

	def angle(self):
		return phase(self)

	def conjugate(self):
		return conjugate(self)

	def conj(self):
		return conjugate(self)

	def polar_coord(self):
		return (self.abs(), self.phase())

	def rect_coord(self):
		return (self.real, self.imag)

	def __abs__(self):
		return module(self)

	def __neg__(self):
		return Complex(-self.real, -self.imag)

	def __add__(self, z):
		z = real_to_complex(z)

		return Complex(self.real + z.real, self.imag + z.imag)

	def __radd__(self, z):
		return self + z

	def __mul__(self,z):
		z = real_to_complex(z)

		return Complex(self.real*z.real - self.imag*z.imag, 
			self.real*z.imag + self.imag*z.real)

	def __rmul__(self,z):
		return self*z

	def __sub__(self, z):
		z = real_to_complex(z)
		
		return Complex(self.real - z.real, self.imag - z.imag)

	def __rsub__(self,z):
		return -self + z

	def __truediv__(self, z):
		z = real_to_complex(z)

		return self*z**-1

	def __rtruediv__(self, z):
		return self**-1*z

	def __pow__(self, z):
		z = real_to_complex(z)

		return exp(z*Ln(self))

	def __rpow__(self, z):
		z = real_to_complex(z)

		return exp(self*Ln(z))

	def __eq__(self,z):
		z = real_to_complex(z)

		# We use this, since real and imaginary parts tend to be floats
		return (m.isclose(z.real,self.real, abs_tol=self.precission) 
			and m.isclose(z.imag ,self.imag, abs_tol=self.precission))	

	def __repr__(self):
		return str(self)

	def __str__(self):
		sign = ' - ' if self.imag < 0 else ' + '
		return str(self.real) + sign + str(abs(self.imag)) + Complex.symbol		

	def __init__(self, r, i=0):
		# Since sin(pi) != 0, but a number very very small, we put this guard.
		if abs(r) < Complex.precission: r = 0
		if abs(i) < Complex.precission: i = 0

		if isinstance(r, Complex): r = r.to_float
		if isinstance(i, Complex): i = i.to_float

		self.imag = float(i)
		self.real = float(r)

C = Complex
j = i = I = J = Complex(0,1)
pi = m.pi
pi2 = 2*m.pi