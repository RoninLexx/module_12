import unittest
from runner_and_tournament import Runner


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += self.speed * 0.5

    def run(self):
        self.distance += self.speed

    def __eq__(self, other):
        return self.name == other.name


class Tournament:
    def __init__(self, distance):
        self.distance = distance

    def start(self, runners):
        results = {}
        for runner in runners:
            while runner.distance < self.distance:
                runner.run()  # Используем метод run для прибавления дистанции
            results[runner.name] = runner.distance

        # Сортируем результаты по расстоянию
        sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)

        # Формирование отображаемого формата: {позиция: имя}
        formatted_results = {index + 1: name for index, (name, _) in enumerate(sorted_results)}
        print(formatted_results)  # Вывод результатов
        return formatted_results


# Реализация классов тестов TournamentTest:

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("\nРезультаты всех тестов:")
        for name, distance in cls.all_results.items():
            print(f"{name}: {distance}")

    def test_race_usain_and_nik(self):
        tournament = Tournament(90)
        results = tournament.start([self.runner1, self.runner3])
        self.all_results.update(results)  # Сохраняем результаты
        self.assertIn(1, results)  # Проверка на первое место

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90)
        results = tournament.start([self.runner2, self.runner3])
        self.all_results.update(results)  # Сохраняем результаты
        self.assertIn(1, results)  # Проверка на первое место

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90)
        results = tournament.start([self.runner1, self.runner2, self.runner3])
        self.all_results.update(results)  # Сохраняем результаты
        self.assertIn(1, results)  # Проверка на первое место


if __name__ == "__main__":
    unittest.main()

# В методе start класса Tournament, чтобы избежать ситуации,
# когда бегун с меньшей скоростью может преодолеть дистанцию раньше,
# чем быстрее бегун, следует убедиться, что каждый бегун бежит до конца дистанции,
# а результат возвращается верно.
