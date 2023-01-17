from shopping_cart_unittest_hw import show, add, delete, shopping_cart
import unittest
from class_shopping import Cart

my_stuff = Cart()

class Shopping_cart_test(unittest.TestCase):
    def test_add(self):
        my_stuff.add("pear", 3, 4)
        self.assertIn("pear", my_stuff.items )

        my_stuff.add("apple", 2, 2)
        self.assertIn("apple", my_stuff.items )

        my_stuff.add("sneakers", 1, 1)
        self.assertIn("sneakers", my_stuff.items )

        my_stuff.add("computer", 1, 1)
        self.assertIn("computer", my_stuff.items )
