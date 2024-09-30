import unittest
from functions import tdd

class test_SumofEven(unittest.TestCase):
    
    def test_Even_numbers_addition(self):
        self.assertEqual(tdd.sum_of_even([7, 6, 2, 3, 8, 3, 9]), 16) #random numbers test
        self.assertEqual(tdd.sum_of_even([2, 4, 4]), 10) #even numbers test
        self.assertEqual(tdd.sum_of_even([3, 5, 9]), 0) #Odd numbers test
        self.assertEqual(tdd.sum_of_even([-1, -2, -3, -4, -5]), -6) #negative numbers
        self.assertEqual(tdd.sum_of_even([]), 0) #empty list

    def test_median(self):
        self.assertEqual(tdd.calculate_mediam([]), None) #empty list
        self.assertEqual(tdd.calculate_mediam([3]), 3) #random single number
        self.assertEqual(tdd.calculate_mediam([6, 6, 6, 6]), 6) #same number
        self.assertEqual(tdd.calculate_mediam([1,2,3,4,5]), 3) #odd length of numbers

    def test_Missing_number(self):
        self.assertEqual(tdd.first_non_repeating_char([]), None)
        self.assertEqual(tdd.first_non_repeating_char([2]), 1)
        self.assertEqual(tdd.first_non_repeating_char([2,3,4,5]), 1)
        self.assertEqual(tdd.first_non_repeating_char([5,6,3,7,2,1]), 4)

    def test_duplicates(self):
        self.assertEqual(tdd.remove_duplicates(""), "")
        self.assertEqual(tdd.remove_duplicates("!@#$&*'"), "!@#$&*'")
        self.assertEqual(tdd.remove_duplicates("aaaaaaaaaaa"), "a")
        self.assertEqual(tdd.remove_duplicates("LeSEtja"), "LeSEtja")


    def test_first_non_repeat(self):
        self.assertEqual(tdd.first_non_repeat(""), None)
        self.assertEqual(tdd.first_non_repeat("aaaaaaaaa"), None)
        self.assertEqual(tdd.first_non_repeat("pineapple"), "i")
        self.assertEqual(tdd.first_non_repeat("e"), "e")



if __name__ == "__main__":
    unittest.main()