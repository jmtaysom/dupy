import unittest
from pathlib import Path

from du import children_size, find_children, format_file_size


class TestDuFunctions(unittest.TestCase):

    def test_find_children(self):
        p = Path('./data')
        children = find_children(p)
        self.assertEqual(children[0].name, 'data')
        self.assertEqual(len(children), 3)

    def test_children_size(self):
        p = Path('./data')
        size = children_size(p)
        self.assertEqual(size, 4060288)

    def test_format_file_size(self):
        p = Path('./data/child/grandchild')
        formatted_size = format_file_size(p, 1024)
        self.assertEqual(formatted_size[0][:3], '40 ')

    def test_format_file_size_readable(self):
        p = Path('./data/child/grandchild')
        formatted_size = format_file_size(p, 1024, 'K')
        self.assertEqual(formatted_size[0][:3], '40K')

    def test_format_file_size_MB(self):
        p = Path('./data')
        formatted_size = format_file_size(p, 1024**2)
        self.assertEqual(formatted_size[0][:3], '4  ')


if __name__ == '__main__':
    unittest.main()