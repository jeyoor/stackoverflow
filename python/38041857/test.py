import unittest
import dict_count


class TestSimpleDictCounter(unittest.TestCase):

    def setUp(self):
        self.counter = dict_count.SimpleDictCounter()

    def test_init(self):
        self.assertEqual(len(self.counter.number_found), 0)

    def test_count_occur(self):
        self.counter._count_occurences('elephant')
        self.counter._count_occurences('elephant')
        self.assertEqual(self.counter.number_found['elephant'], 2)

class TestBetterDictCounter(unittest.TestCase):

    def setUp(self):
        self.counter = dict_count.BetterDictCounter()

    def test_init(self):
        self.assertEqual(len(self.counter.number_found), 0)

    def test_count_occur(self):
        self.counter._count_occurences('elephant')
        self.counter._count_occurences('elephant')
        self.assertEqual(self.counter.number_found['elephant'], 2)

if __name__ == '__main__':
    unittest.main()
