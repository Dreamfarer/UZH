from unittest import TestCase

class PublicTestSuite(TestCase):

    def test_price_is_number(self):
        from public import script
        x = script.get_price()
        print(isinstance(x, (int, float))
              and not isinstance(x, bool))

