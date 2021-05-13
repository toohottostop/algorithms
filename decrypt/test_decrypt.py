import unittest

from decrypt import decrypt


class TestDecrypt(unittest.TestCase):
    def test_algorithm(self):
        self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра........'), '')
        self.assertEqual(decrypt('абр......a.'), 'a')
        self.assertEqual(decrypt('1..2.3'), '23')
        self.assertEqual(decrypt('.'), '')
        self.assertEqual(decrypt('1.......................'), '')
        self.assertEqual(decrypt('а.б.р.а.а..-.к.а.д.а.б.р.а.'), 'абра-кадабра')
