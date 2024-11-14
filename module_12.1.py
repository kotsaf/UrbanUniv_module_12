import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


'''TESTS'''
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        begun1 = Runner('misha')
        for _ in range(10):
            begun1.walk()
        self.assertEqual(begun1.distance, 50)

    def test_run(self):
        begun2 = Runner('sasha')
        for _ in range(10):
            begun2.run()
        self.assertEqual(begun2.distance, 100)

    def test_challenge(self):
        begun3 = Runner('denis')
        begun4 = Runner('max')
        for _ in range(10):
            begun3.run()
            begun4.walk()
        self.assertNotEqual(begun3.distance, begun4.distance)


if __name__ == '__main__':
    unittest.main()