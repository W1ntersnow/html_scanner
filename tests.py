import unittest
import helpers


class TestHelpers(unittest.TestCase):

    def test_load_stop_word(self):
        expected_result = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and']
        file_name = 'unit_test_file.txt'
        with open(file_name, 'w') as file:
            [file.write('{}\n'.format(value)) for value in expected_result]
        case_result = helpers.load_stop_word(file_name)
        self.assertEqual(case_result, expected_result)
