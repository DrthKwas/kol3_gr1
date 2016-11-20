from unittest import TestCase

from diary import Diary
from student import Student
from subject import Subject


class TestDiary(TestCase):
    def setUp(self):
        self.EPSILON = 0.01
        sub1 = Subject("Biologia", [[3.5, 2.5, 5.0], [1, 1, 1, 1, 1, 1, 1, 1, 0]])
        sub2 = Subject("Matematyka", [[2.5, 3.0, 2.5], [1, 1, 0, 1, 0, 1, 0, 1, 1]])
        self.subjects = [sub1, sub2]
        self.andrzej = Student("Andrzej Abacki", self.subjects)
        self.diary = Diary("AGH", 2016, "data.json")

    def test_init(self):
        self.assertEqual(self.diary.get_student("Andrzej Abacki").name, self.andrzej.name)
        self.assertEqual(len(self.diary.get_student("Andrzej Abacki").subjects), len(self.andrzej.subjects))

    def test_franciszek_compute_total_average(self):
        self.assertAlmostEquals(self.diary.get_student("Franciszek Fabacki").compute_total_average(), 3.83, 2)

    def test_get_not_existing_student(self):
        self.assertIsNone(self.diary.get_student("Klima Nima"))
