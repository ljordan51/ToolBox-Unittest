import unittest


def sort_and_rm_neg_num(num_list):
    edited = []
    for num in num_list:
        if num >= 0:
            edited.append(num)
    return sorted(edited)


class TestMethod(unittest.TestCase):

    def test_func(self):
        self.assertEqual(sort_and_rm_neg_num([3, -4, 2, 6, -1, -8, 7, 3, 2, 1]), [1, 2, 2, 3, 3, 6, 7])


if __name__ == '__main__':
    unittest.main()
