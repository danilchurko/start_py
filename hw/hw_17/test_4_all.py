import unittest
from hw.hw_6 import task1 as tr1
from hw.hw_7 import task2 as tr2
from hw.hw_11 import task2 as tr3
from hw.hw_15 import task2 as tr4


class Testing6(unittest.TestCase):

    def currency_test(self):
        coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
        code = ('BTC', 'ETH', 'XRP', 'LTC')
        self.assertEqual(tr1.make_dict(coin, code),
                         {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'})



class Testing7(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(tr2.convert(43, 'C'), 'Temperature. C to F: ')

    def test_celsius_to_kelvin(self):
        self.assertEqual(tr2.convert(223, 'C'), 'Temperature. C to K: ')

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(tr2.convert(60, 'F'), 'Temperature. F to C: ')

    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(tr2.convert(85, 'F'), 'Temperature. F to K: ')

    def test_kelvin_to_celsius(self):
        self.assertEqual(tr2.convert(123, 'K'), 'Temperature. K to C: ')

    def  kelvin_to_fahrenheit(self):
        self.assertEqual(tr2.convert(45, 'K'), 'Temperature. K to F:  ')



class Testing11(unittest.TestCase):

    def email_test(self):
        self.assertEqual(tr3.hide_email('what_is_the_name_of_half-life_speedrun@a_minute_of_silence.com'),
                         'wh**@**e.com')

class Testing15(unittest.TestCase):

    def phone_test(self):
        self.assertEqual((tr4.telephone('063-999-99-99'), '(+38) 063 999-99-99'),
        self.assertEqual((tr4.telephone('063 999-99-99'), '(+38) 063 999-99-99'),
        self.assertEqual((tr4.telephone('063-99999-99'), '(+38) 063 999-99-99'),
        self.assertEqual((tr4.telephone('+3806399999-99'), '(+38) 063 999-99-99'),
        self.assertEqual((tr4.telephone('380639999999'), '(+38) 063 999-99-99')

if __name__ == '__main__':
    unittest.main()