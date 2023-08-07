import unittest
import file_

class TestNewClass(unittest.TestCase):
    # def setUp(self):
    #     print('I\'m setting something up')

    def testGuessingSameNumber(self):
        question = 8
        answer = 8
        result = file_.guessing_game(question=question, answer=answer)
        self.assertTrue(result)
    
    def testGuessingDiffNumer(self):
        result = file_.guessing_game(question=8, answer=5)
        self.assertFalse(result)
    
    def testGuessingOutofRange(self):
        result = file_.guessing_game(question=89, answer=5)
        self.assertFalse(result)
    
    def testGuessingIfString(self):
        result = file_.guessing_game(question=8, answer='kjkyh')
        self.assertFalse(result)
    
    # def testGuessingGame3(self):
    #     result = file_.guessing_game(question='jbyivu', answer=5)
    #     self.assertIsInstance(result, ValueError)
        # self.assertEqual(result, 'I want a number, Silly!')

    def testing_for1(self):
        numb = 6
        result = file_.simple_add(numb)
        self.assertEqual(result, 11)

    def testing_for2(self):
        numb = 'gibbrish'
        result = file_.simple_add(numb)
        self.assertIsInstance(result, ValueError)

    def testing_for3(self):
        numb = None
        result = file_.simple_add(numb)
        self.assertEqual(result, 'Please enter a number')

    def testing_for4(self):
        numb = ''
        result = file_.simple_add(numb)
        self.assertEqual(result, 'Please enter a number')

    def testing5(self):
        numb = 0
        result = file_.simple_add(numb)
        self.assertEqual(result, 5)

    # def tearDown(self):
    #     print('I\'m cleaning up')

if __name__ == '__main__':
    unittest.main()