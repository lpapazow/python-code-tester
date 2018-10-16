import unittest

class Testw1t1(unittest.TestCase):
    def test_sum_of_digits_long_number(self):       
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(sum_of_digits(1325132435356), 43)""")

    def test_sum_of_digits(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(sum_of_digits(123), 6)""")
        
    def test_sum_of_digits_negative_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(sum_of_digits(-10), 1)""")
        
    def test_sum_of_digits_negative_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(sum_of_digits(-11), 2)""")
        
    def test_to_digits_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(to_digits(123), [1, 2, 3])""")
        
    def test_to_digits_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(to_digits(99999), [9, 9, 9, 9, 9])""")

    def test_to_digits_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])""")               

class Testw1t2(unittest.TestCase):
    def test_word_counter_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(word_counter('''ivan
5 4
i v    a n
e v n h
i n    a v
m v    v n
q r    i t'''), 3)""")

    def test_word_counter_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(word_counter('''actually
8 15
i v a n q h r e z g t z o y m
e v n h t r x e k y d a i l c
i a c t u a l l y m c x r l e
m v c n p u a m n t l u e a a
q r i t w e a q u p r x t u z
p e a c t u a l l y w p y t m
o y h t r e l u f p q n z c s
p a c t u a l l y u r e q a r'''), 4)""")

    def test_word_counter_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(word_counter('''madam
8 12
z v a n q h r e z g t z
e v m h t r x e k y m a
i a c a u a l l y a c x
m v c n d u a m d t l u
q t i t w a a a u p r x
p e m a d a m l l y w p
o y h t e e l u f p q n
p a c t u a l l y u r e'''), 3)""")

    def test_prime_factorization_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(prime_factorization(10), [(2, 1), (5, 1)])""")

    def test_prime_factorization_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(prime_factorization(356), [(2, 2), (89, 1)])""")
        
    def test_prime_factorization_3(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(prime_factorization(89), [(89, 1)])""")
        
    def test_sum_matrix_1(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)""")

    def test_sum_matrix_2(self):
        with open('codetester/htmlparser/tempcode.py', 'r') as myfile:
            data=myfile.read()
        exec(data)
        exec("""self.assertEqual(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)""")
        
class Testw1t3(unittest.TestCase):
    pass
    
class Testw1t4(unittest.TestCase):
    pass
    
class Testw2t3(unittest.TestCase):
    pass