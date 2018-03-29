import unittest
from AlComplex import * 

a = Complex(0,1)
b = Complex(1,0)
c = Complex(1,1)
d = Complex(2,3)
e = Complex(1)

class TestFuncs(unittest.TestCase):
	def test_initiation(self):

		self.assertEqual(a+b, c)
		self.assertEqual(a-b, Complex(-1,1))
		self.assertEqual(j+4, C(4,1))
		self.assertEqual(j+4.123, C(4.123,1))
		self.assertEqual(j+m.sqrt(4.123), C(m.sqrt(4.123),1))

		self.assertEqual(d*d, Complex(-5,12))
		self.assertEqual(Complex(900)*4, Complex(3600))
		self.assertEqual(3*C(9,8), C(27,24))
		self.assertEqual(C(1,0)*C(0,1), C(0,1))
	
		self.assertEqual(i/i, 1)
		self.assertEqual(1/i, -i)
		self.assertEqual((3-i)/(2+3*i)+(2-2*i)/(1-5*i), 9/13 - 7/13*i)

		self.assertEqual(i**2, -1)
		self.assertEqual((-1)**Complex(0,3), exp(-m.pi*3))
		self.assertEqual((-i)**i, exp(m.pi/2))

		self.assertEqual(C(4)**1/2, 2)

	def test_polar(self):
		self.assertEqual(Complex.polar(1,0), Complex(1,0))

	def test_exp(self):
		self.assertEqual(exp(1), m.exp(1))
		self.assertEqual(exp(0), 1)
		self.assertEqual(exp(0+m.pi*i), -1)
		self.assertEqual(exp(m.log(3) - m.pi/2*i), C(0,-3))
		self.assertEqual(4*exp(m.pi/4*i), Complex.polar(4, m.pi/4))

	def test_Ln(self):
		self.assertEqual(Ln(1), 0)
		self.assertEqual(Ln(exp(4+i)), 4+i)
		self.assertEqual(Ln(-1), m.pi*i)
		self.assertEqual(Ln(-i), -m.pi/2*i)

	def test_exponential(self):
		self.assertEqual(i**-1, -i)
		self.assertEqual(C(4)**-1, 1/4)

	def test_trignonometric(self):
		self.assertEqual(sin(0), 0)
		self.assertEqual(sin(m.pi/2), 1)
		self.assertEqual(cos(0), 1)
		self.assertEqual(cos(m.pi), -1)
		self.assertEqual(tan(0), 0)
		self.assertEqual(tan(1+i), sin(1+i)/cos(1+i))
		self.assertEqual(tan(m.pi/4), 1)

		self.assertEqual(sin(4*i), 1/2*(m.exp(4)-m.exp(-4))*i)

		self.assertEqual(-i*sinh(i*a), sin(a))
		self.assertEqual(cos(b), cosh(i*b))
		self.assertEqual(sinh(c), -i*sin(i*c))
		self.assertEqual(cosh(d), cos(d*i))

	def test_roots(self):
		l1 = list(roots(1, 3))
		l2 = list(roots(i, 2))
		l5 = list(roots(i+2, 10))

		with self.assertRaises(Exception):
			list(roots(i, 0))

		self.assertEqual(len(l1), 3)
		self.assertEqual(len(l5), 10)
		self.assertEqual(l1[0]**3, 1)
		self.assertEqual(l2[1]**2, i)
		self.assertEqual(l5[3]**10,i+2)

	def test_ln(self):
		self.assertEqual(ln_n_branch(1,0), 0)
		self.assertEqual(ln_n_branch(exp(4+i), 0), 4+i)
		self.assertEqual(ln_n_branch(exp(4+i), 1), 4+i+2*m.pi*i)

		l1 = list(ln_values(i+12, 3, 7))
		l2 = list(ln_values(i, 6, 2))
		l3 = list(ln_values(i, -2, 3))

		self.assertEqual(len(l1), len(l2))
		for k in l1:
			self.assertEqual(exp(k), i+12)

		self.assertIn(-7*m.pi/2*i, l3)
		self.assertIn(-3*m.pi/2*i, l3)
		self.assertIn(m.pi/2*i, l3)
		self.assertIn(5*m.pi/2*i, l3)