from unittest import TestCase

from student import Student
from subject import Subject


class TestStudent(TestCase):
    def setUp(self):
        self.EPSILON = 0.01
        sub1 = Subject("ZTI", [[4, 5, 5], [0, 1, 1, 1, 1]])
        sub2 = Subject("PITE", [[4.5, 5, 5, 4], [1, 1, 1, 1, 1]])
        self.subjects = [sub1, sub2]
        self.student = Student("Adam Abacki", self.subjects)

    def test_compute_total_average(self):
        self.assertAlmostEquals(self.student.compute_total_average(), 32.5 / 7, 2)

    def test_compute_ZTI_average(self):
        self.assertAlmostEquals(self.student.compute_subject_average("ZTI"), 14. / 3, 2)

    def test_compute_PITE_average(self):
        self.assertAlmostEquals(self.student.compute_subject_average("PITE"), 18.5 / 4, 2)

    def test_compute_total_attendance(self):
        self.assertEqual(self.student.compute_total_attendance(), 90)

    def test_compute_ZTI_attendance(self):
        self.assertEqual(self.student.compute_subject_attendance("ZTI"), 80)

    def test_compute_PITE_attendance(self):
        self.assertEqual(self.student.compute_subject_attendance("PITE"), 100)
