import unittest

class Runner:

    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:

    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        running_time = 0
        place = 1
        while self.participants:
            running_time += 1
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


'''TESTS'''
class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i, f in cls.all_results.items():
            print(f"{i}")
            for e, d in f.items():
                print(f"{e}: {d}")

    def setUp(self):
        self.runners = [
            Runner('Usain', 10),
            Runner('Andrei', 9),
            Runner('Nick', 3)
        ]

    def test_run1(self):
        turnir1 = Tournament(90, self.runners[0], self.runners[2])
        zabeg = turnir1.start()
        self.assertTrue(list(zabeg.values())[-1].name== 'Nick')
        self.all_results[self.runners[0].name, self.runners[2].name] = zabeg

    def test_run2(self):
        turnir2 = Tournament(90, self.runners[1], self.runners[2])
        zabeg = turnir2.start()
        self.assertTrue(list(zabeg.values())[-1].name== 'Nick')
        self.all_results[self.runners[1].name, self.runners[2].name] = zabeg

    def test_run3(self):
        turnir3 = Tournament(90, self.runners[0], self.runners[1], self.runners[2])
        zabeg = turnir3.start()
        self.assertTrue(list(zabeg.values())[-1].name== 'Nick')
        self.all_results[self.runners[0].name, self.runners[1].name, self.runners[2].name] = zabeg




if __name__ == '__main__':
    unittest.main()
