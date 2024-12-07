import unittest

from advent_of_code2024.day2.main import Report, Level


class MyTestCase(unittest.TestCase):

    def create_first_example_report(self):
        report = Report()
        for value in (7, 6, 4, 2, 1):
            report.add_level(level=Level(value))
        return report

    def create_second_example_report(self):
        report = Report()
        for value in (1, 2, 7, 8, 9):
            report.add_level(level=Level(value))
        return report

    def create_third_example_report(self):
        report = Report()
        for value in (9, 7, 6, 2, 1):
            report.add_level(level=Level(value))
        return report

    def create_forth_example_report(self):
        report = Report()
        for value in (1, 3, 2, 4, 5):
            report.add_level(level=Level(value))
        return report

    def create_fifth_example_report(self):
        report = Report()
        for value in (8, 6, 4, 4, 1):
            report.add_level(level=Level(value))
        return report

    def create_sixth_example_report(self):
        report = Report()
        for value in (1, 3, 6, 7, 9):
            report.add_level(level=Level(value))
        return report

    def test_first_example(self):
        a_report = self.create_first_example_report()

        self.assertTrue(a_report.is_safe())

    def test_second_example(self):
        a_report = self.create_second_example_report()

        self.assertFalse(a_report.is_safe())

    def test_third_example(self):
        a_report = self.create_second_example_report()

        self.assertFalse(a_report.is_safe())

    def test_fourth_example(self):
        a_report = self.create_forth_example_report()

        self.assertTrue(a_report.is_safe())

    def test_fifth_example(self):
        a_report = self.create_fifth_example_report()

        self.assertTrue(a_report.is_safe())

    def test_sixth_example(self):
        a_report = self.create_sixth_example_report()

        self.assertTrue(a_report.is_safe())

    def create_bizarre(self):
        report = Report()
        for value in (12, 12, 14, 16, 17, 18):
            report.add_level(level=Level(value))
        return report

    def test_bizarre(self):
        a_report = self.create_bizarre()

        self.assertTrue(a_report.is_safe())
