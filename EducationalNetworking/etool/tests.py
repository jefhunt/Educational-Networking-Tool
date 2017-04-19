from django.test import TestCase


# Create your tests here.
#example for test case
class Demotest(TestCase):
	def testAd(self):
		self.assertEqual(1+2,3)
		self.assertEqual(2+3,5)

	
