import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        # Создаем объект Runner
        runner = Runner("Test Runner")

        # Выполняем метод walk 10 раз
        for _ in range(10):
            runner.walk()

        # Проверяем, что distance равен 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        # Создаем объект Runner
        runner = Runner("Test Runner")

        # Выполняем метод run 10 раз
        for _ in range(10):
            runner.run()

        # Проверяем, что distance равен 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        # Создаем два объекта Runner
        runner1 = Runner("Test Runner 1")
        runner2 = Runner("Test Runner 2")

        # Выполняем метод run для первого объекта и walk для второго 10 раз
        for _ in range(10):
            runner1.run()
            runner2.walk()

        # Проверяем, что расстояния различаются
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
    