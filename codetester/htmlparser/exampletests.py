import unittest

class Testw1t1(unittest.TestCase):
    def test_sum_of_digits_long_number(self):       
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_of_digits(1325132435356), 43)

    def test_sum_of_digits(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_of_digits(123), 6)
        
    def test_sum_of_digits_negative_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_of_digits(-10), 1)
        
    def test_sum_of_digits_negative_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_of_digits(-11), 2)
        
    def test_to_digits_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(to_digits(123), [1, 2, 3])
        
    def test_to_digits_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(to_digits(99999), [9, 9, 9, 9, 9])

    def test_to_digits_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])             

class Testw1t2(unittest.TestCase):
    def test_word_counter_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(word_counter('''ivan
5 4
i v    a n
e v n h
i n    a v
m v    v n
q r    i t'''), 3)

    def test_word_counter_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(word_counter('''actually
8 15
i v a n q h r e z g t z o y m
e v n h t r x e k y d a i l c
i a c t u a l l y m c x r l e
m v c n p u a m n t l u e a a
q r i t w e a q u p r x t u z
p e a c t u a l l y w p y t m
o y h t r e l u f p q n z c s
p a c t u a l l y u r e q a r'''), 4)

    def test_word_counter_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(word_counter('''madam
8 12
z v a n q h r e z g t z
e v m h t r x e k y m a
i a c a u a l l y a c x
m v c n d u a m d t l u
q t i t w a a a u p r x
p e m a d a m l l y w p
o y h t e e l u f p q n
p a c t u a l l y u r e'''), 3)

    def test_word_counter_no_diagonals(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        print("Will execute!")
        ldict={}
        exec(data, globals(), globals())
        print(ldict)
        self.assertEqual(word_counter('''peron
8 12
p p e r o n r e z g t z
e v m h t r x e k y m a
r a c a u a l l y a c x
o v c n d u a m d t l u
n t i t w a a a u p r x
p e m a d a m l l y w p
o y h p e r o n f p q n
p a c t u a l l y u r e'''), 3)


    def test_prime_factorization_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(prime_factorization(10), [(2, 1), (5, 1)])

    def test_prime_factorization_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(prime_factorization(356), [(2, 2), (89, 1)])
        
    def test_prime_factorization_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(prime_factorization(89), [(89, 1)])
        
    def test_sum_matrix_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)

    def test_sum_matrix_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)
        
class Testw1t3(unittest.TestCase):
    def test_is_number_balanced_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertTrue(is_number_balanced(9))
        
    def test_is_number_balanced_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertTrue(is_number_balanced(44))
        
    def test_is_number_balanced_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertTrue(is_number_balanced(4518))
        
    def test_is_number_balanced_4(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertFalse(is_number_balanced(28471))
        
    def test_is_number_balanced_5(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertFalse(is_number_balanced(221))
    
    def test_is_number_balanced_6(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertTrue(is_number_balanced(1238033))
        
    def test_increasing_or_decreasing_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(increasing_or_decreasing([1,2,3,4,5]), 'Up!')
        
    def test_increasing_or_decreasing_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(increasing_or_decreasing([5,6,-10]), False)

    def test_increasing_or_decreasing_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(increasing_or_decreasing([1, 1, 1]), False)
        
    def test_increasing_or_decreasing_4(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(increasing_or_decreasing([1, 1, 1]), False)

    def test_increasing_or_decreasing_5(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(increasing_or_decreasing([9,8,7,6]), 'Down!')
        
    def test_largest_palindrome_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(get_largest_palindrome(99), 88)

    def test_largest_palindrome_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(get_largest_palindrome(994687), 994499)
        
    def test_largest_palindrome_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(get_largest_palindrome(754649), 754457)
        
    def test_sum_of_numbers_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_of_numbers("ab125cd3"), 128)
        
    def test_sum_of_numbers_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_of_numbers("ab12"), 12)
        
    def test_sum_of_numbers_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(sum_of_numbers("pe6o"), 0)
        
    def test_birthday_ranges_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]), [2, 3, 4, 5, 2])        
         
    def test_birthday_ranges_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]), [5, 2, 0, 1])

    def test_numbers_to_message_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]), "abc")
        
    def test_numbers_to_message_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(numbers_to_message([2, 2, 2, 2]), "a")
        
    def test_numbers_to_message_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]), "Ivo e Panda")
        
    def test_message_to_numbers_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(message_to_numbers("abc"), [2, -1, 2, 2, -1, 2, 2, 2])
        
    def test_message_to_numbers_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(message_to_numbers("a"), [2])
        
    def test_message_to_numbers_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(message_to_numbers("Ivo e Panda"), [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2])
        
    def test_message_to_numbers_4(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data, globals())
        self.assertEqual(message_to_numbers("aabbcc"), [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2])

        
class Testw1t4(unittest.TestCase):
    pass
    
class Testw2t3(unittest.TestCase):
    pass