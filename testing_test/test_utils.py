import unittest

from testing_test.exception import MyCustomException
from . import utils
from . import util


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(True, True)  # add assertion here

    def test_add_func(self):
        # """
        # GIVEN:
        # >>> x.utils
        # WHEN:
        # >>> utils.add(8, 8)
        # THEN:
        # >>> assertEqual(12, x)
        # :return:
        # """
        x = utils.add(5, 7)
        self.assertEqual(12, x)
        self.assertAlmostEqual(0.1 + 0.2, 0.4, 2)

    def test_that_add_throws_exception(self):
        # self.assertRaises(TypeError, util.add(2, '3'))

        with self.assertRaises(TypeError):
            utils.add(2, 'hi')

        with self.assertRaises(MyCustomException):
            utils.add(6, 2)


if __name__ == '__main__':
    unittest.main()
