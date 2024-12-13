import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Часть 1: TestSuite
test_suite = unittest.TestSuite()
test_suite.addTest(RunnerTest('test_challenge'))
test_suite.addTest(RunnerTest('test_run'))
test_suite.addTest(RunnerTest('test_walk'))
test_suite.addTest(TournamentTest('test_first_tournament'))
test_suite.addTest(TournamentTest('test_second_tournament'))
test_suite.addTest(TournamentTest('test_third_tournament'))

# Часть 2: Пропуск тестов
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
