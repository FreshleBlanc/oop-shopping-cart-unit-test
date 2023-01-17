from main import add, subtract, multiply, divide

from address_book import store_user_info, remove_user_info, address_book

import unittest

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        result1 = add(1,5)
        self.assertEqual(result1,6)

        result2 = add(-10,5)
        self.assertEqual(result2,-5)

        result3 = add(-10,-5)
        self.assertEqual(result3,-15)

        result4 = add(4.5, 5.2)
        self.assertEqual(result4,9.7)


    def test_subtract(self):
        result5 = subtract(8,2)
        self.assertEqual(result5,6)
        
        result6 = subtract(15,5)
        self.assertEqual(result6,10)

    def test_multiplu(self):
        result7 = multiply(9,3)
        self.assertEqual(result7,27)

        result8 = multiply(2,12)
        self.assertEqual(result8,24)

    def test_divide(self):
        result9 = divide(9,3)
        self.assertEqual(result9,3)

        result10 = divide(16,4)
        self.assertEqual(result10,4)


class AddressBookTest(unittest.TestCase):
    
    def test_store_user_info(self):
        store_user_info('dylan', '123 1st St')
        self.assertIn('dylan', address_book)
        
        store_user_info('chris', '55 2nd st')
        self.assertIn('chris', address_book)

        self.assertNotIn('johnny', address_book)

    def test_remove_user_info(self):
        test_address_book = {}
        test_address_book['jen'] = '123 main st'
        test_address_book['debra'] = '321 alternative st'
        self.assertIn('jen', test_address_book)
        remove_user_info('jen')
        self.assertNotIn('jen', test_address_book)









unittest.main()
