#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_random_number, test_config
from src.question_b.question_b import get_assesment_vaule, get_tax_assesed
from src.question_d.question_d import rev_str
from src.question_c.question_c import get_fahrenheit


class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_random_number(self):
        self.assertTrue(get_random_number() in range(1,6))

    def test_get_assesment_value(self):
        self.assertEqual(get_assesment_vaule(10000), 6000)
        self.assertEqual(get_assesment_vaule(20000), 12000)

    def test_get_tax_assesed(self):
        self.assertEqual(get_tax_assesed(6000), 43.2)
        self.assertEqual(get_tax_assesed(10000), 72)

    def test_rev_str(self):
        self.assertEqual("dlrow olleh", rev_str("hello world"))

    def test_get_fahernheit(self):
        self.assertEqual(get_fahrenheit(0), 32)
        self.assertEqual(get_fahrenheit(5), 41)
        self.assertEqual(get_fahrenheit(10), 50)