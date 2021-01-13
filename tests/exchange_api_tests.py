from utils.list import chunk_list

import unittest


class TestChunkList(unittest.TestCase):
    def test_chunk_list_empty_list(self):
        test_list = []
        expected_restult = []

        chunked_lists = [c for c in chunk_list(test_list, size=10)]
        self.assertListEqual(expected_restult, chunked_lists)

    def test_chunk_list_less_than_size(self):
        test_list = [1, 2, 3]
        expected_restult = [[1,2, 3]]

        chunked_lists = [c for c in chunk_list(test_list, size=10)]
        self.assertListEqual(expected_restult, chunked_lists)

    def test_chunk_list_chunking_list(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_restult = [[1,2, 3], [4, 5, 6], [7, 8, 9]]

        chunked_lists = [c for c in chunk_list(test_list, size=3)]
        self.assertListEqual(expected_restult, chunked_lists)

