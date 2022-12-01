from unittest import TestCase

class PublicTestSuite(TestCase):

    def test_output_is_number(self):
        from public import script
        output = script.calculate()
        self.assertTrue(
            isinstance(output, (int, float)) and
            not isinstance(output, bool) and
            not isinstance(output, str))

