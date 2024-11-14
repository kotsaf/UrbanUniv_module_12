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
        i = 0
        while i < 10:
            begun1.walk()
            i += 1
        self.assertEqual(begun1.distance, 50)

    def test_run(self):
        begun2 = Runner('sasha')
        i = 0
        while i < 10:
            begun2.run()
            i += 1
        self.assertEqual(begun2.distance, 100)

    def test_challenge(self):
        begun3 = Runner('denis')
        begun4 = Runner('max')
        i = 0
        while i < 10:
            begun3.run()
            begun4.walk()
            i += 1
        self.assertNotEqual(begun3.distance, begun4.distance)


if __name__ == '__main__':
    unittest.main()