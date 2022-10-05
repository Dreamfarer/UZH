from unittest import TestCase
import inspect

class PublicTestSuite(TestCase):

    def test_assertion_is_true(self):
        from public import script
        source = inspect.getsource(script)
        m = "@@The solution seems to contain x = 42, please assign something slighty more complex@@"
        self.assertTrue("x=42" not in ''.join(source.split()), m)
        m = "@@x is not exactly 42@@"
        self.assertEqual(script.x, 42, m)

