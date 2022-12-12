import unittest

from check_guess import CheckGuess

class TestCheckGuess(unittest.TestCase):
    user_guess_list = ['pawn', 'king', 'queen']
    shuffled_word_list = ['wpna', 'nigk', 'eneuq']

    def setUp(self):
        self.check_guess = CheckGuess(self.user_guess_list, self.shuffled_word_list)

    def tearDown(self):
        del self.check_guess

    def test_object_created(self):
        assert self.check_guess.user_guess_list == self.user_guess_list
        assert self.check_guess.shuffled_word_list == self.shuffled_word_list

    def test_invalid_object(self):
        with self.assertRaises(ValueError):
            check_guess = CheckGuess('', self.shuffled_word_list)

    def test_invalid_object(self):
        with self.assertRaises(ValueError):
            check_guess = CheckGuess(self.user_guess_list, '')

    def test_invalid_guess(self):
        with self.assertRaises(ValueError):
            check_guess = CheckGuess([''], self.shuffled_word_list)
            check_guess.check_user_guess()

    def test_check_user_guess(self):
        assert self.check_guess.check_user_guess() == True
        

if __name__ == '__main__':
    unittest.main()