from unittest import TestCase

from subject import Subject


class TestSubject(TestCase):
    def setUp(self):
        self.sub1 = Subject("ZTI", [[4, 5, 5], [0, 1, 1, 1, 1]])
        self.sub2 = Subject("PITE", [[4.5, 5, 5, 4], [1, 1, 1, 1, 1]])

    def test_get_average1(self):
        self.assertAlmostEquals(self.sub1.get_average(), 14. / 3, 2)

    def test_get_average2(self):
        self.assertAlmostEquals(self.sub2.get_average(), 18.5 / 4, 2)

    def test_get_attendance1(self):
        self.assertEqual(self.sub1.get_attendance(), 80)

    def test_get_attendance2(self):
        self.assertEqual(self.sub2.get_attendance(), 100)
