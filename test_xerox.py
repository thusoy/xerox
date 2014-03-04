#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xerox
import unittest

class BasicAPITestCase(unittest.TestCase):

    def setUp(self):
        self.text = 'And now for something completely different.'
        
    def test_copy_paste(self):
        xerox.copy(self.text)
        self.assertEqual(xerox.paste(), self.text)

    def test_unicode(self):
        unicode_text = u'Ξεσκεπάζω τὴν ψυχοφθόρα βδελυγμία'
        xerox.copy(unicode_text)
        self.assertEqual(xerox.paste(), unicode_text)

    def test_empty(self):
        xerox.copy('')
        self.assertEqual(xerox.paste(), '')
        
        
if __name__ == '__main__':
    unittest.main()
