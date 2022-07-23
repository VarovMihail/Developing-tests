import unittest
from main import documents, directories, check_document_existance, get_doc_owner_name, get_all_doc_owners_names, \
remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
show_document_info, show_all_docs_info, add_new_doc, secretary_program_start
from unittest.mock import patch, Mock
from parameterized import parameterized

class TestFunction(unittest.TestCase):

    def test_check_document_existance(self):
        result = check_document_existance('2207 876234')
        self.assertTrue(result)


    @parameterized.expand([('2207 876234', True),
                           ('11-2',True),
                           ('5455 028765', False)])
    def test_check_document_existance_2(self, number,etalon):
        result = check_document_existance(number)
        self.assertEqual(result,etalon)













