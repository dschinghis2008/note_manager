import unittest

from tests import notes
from data import save_notes, load_notes
from interface import display_notes, create_note, delete_note, search_notes, update_note
from utils.validate import check_dt_format, check_status
from utils.generate import get_new_id


class UnitTestNoteManager(unittest.TestCase):
    def test_save_and_load(self):
        file = open('tst_note.txt', 'w', encoding='utf-8')
        save_notes(notes, file)
        file.close()
        file = open('tst_note.txt', encoding='utf-8')
        result_notes = load_notes(file)
        file.close()
        self.assertEqual(notes, result_notes)

    def test_view_list_of_notes(self):
        self.assertRaises(Exception, display_notes(notes))

    def test_get_uniq_id(self):
        self.assertGreater(len(get_new_id()), 0)

    def test_validate_format_dt(self):
        self.assertTrue(check_dt_format('01.01.2025', '%d.%m.%Y'))
        self.assertFalse(check_dt_format('01-01-2025', '%d.%m.%Y'))

    def test_validate_status(self):
        self.assertTrue(check_status('new'))
        self.assertFalse(check_status('None'))

    def test_create_note(self):
        new_notes = notes.copy()
        len_before = len(new_notes)
        new_notes.append(create_note(100))
        self.assertTrue(len_before + 1 == len(new_notes))

    def test_delete_note(self):
        new_notes = notes.copy()
        len_before = len(new_notes)
        delete_note('1', 'user1', new_notes)
        self.assertTrue(len(new_notes) == len_before - 1)

    def test_search_notes(self):
        test_list = search_notes(notes, 'user1')
        self.assertEqual(notes[0], test_list[0])
        test_list = search_notes(notes, '4', 'close')
        self.assertEqual(notes[1:3], test_list[0:2])

    def test_update_note(self):
        new_list = notes.copy()
        self.assertRaises(Exception, update_note(new_list[0]))


if __name__ == '__main__':
    unittest.main()
