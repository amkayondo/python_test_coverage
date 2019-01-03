from numbers import add
import unittest

# Unittest Class
class TestNumbers(unittest.TestCase):
    # method to test add
    def test_add(self):
        # the needed result
        result = add(3,2)

        self.assertEquals(result, 5)