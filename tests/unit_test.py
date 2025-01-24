import unittest, datetime, tests, utils.validate

from data import save, load
from interface.display_notes_function import display_notes
from utils.validate import get_new_id, check_dt_format, check_status


class UnitTestNoteManager(unittest.TestCase):
    def test_save_and_load(self):
        #now = datetime.datetime.now().date()

        file = open('tst_note.txt', 'w', encoding='utf-8')
        save(tests.notes, file)
        file.close()
        file = open('tst_note.txt', encoding='utf-8')
        load_notes = load(file)
        self.assertEqual(tests.notes, load_notes)
        file.close()

    def test_view_list_of_notes(self):
        self.assertRaises(Exception, display_notes(tests.notes))

    def test_get_uniq_id(self):
        self.assertGreater(len(get_new_id()),0)

    def test_validate_format_dt(self):
        self.assertTrue(check_dt_format('01.01.2025','%d.%m.%Y'))
        self.assertFalse(check_dt_format('01-01-2025', '%d.%m.%Y'))

    def test_validate_status(self):
        self.assertTrue(check_status('new'))
        self.assertFalse(check_status('None'))



if __name__ == '__main__':
    unittest.main()
