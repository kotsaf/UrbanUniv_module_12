# coding: utf-8
import logging
import unittest
from TournamentTest import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            begun1 = Runner('misha', -5)
            for _ in range(10):
                begun1.walk()
            self.assertEqual(begun1.distance, 50)
            logging.info('test_walk выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            begun2 = Runner(444, 5)
            for _ in range(10):
                begun2.run()
            self.assertEqual(begun2.distance, 100)
            logging.info('test_run выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()


'''runner_tests.log'''
2024-11-15 17:48:47,818 | WARNING | Неверный тип данных для объекта Runner
Traceback (most recent call last):
  File "D:\Projects\H\module_12\test_12.4.py", line 20, in test_run
    begun2 = Runner(444, 5)
             ^^^^^^^^^^^^^^
  File "D:\Projects\H\module_12\TournamentTest.py", line 10, in __init__
    raise TypeError(f'Имя не может быть номером, передано {type(name).__name__}')
TypeError: Имя не может быть номером, передано int
2024-11-15 17:48:47,819 | WARNING | Неверная скорость для Runner
Traceback (most recent call last):
  File "D:\Projects\H\module_12\test_12.4.py", line 10, in test_walk
    begun1 = Runner('misha', -5)
             ^^^^^^^^^^^^^^^^^^^
  File "D:\Projects\H\module_12\TournamentTest.py", line 15, in __init__
    raise ValueError(f'Скорость не может быть отрицательной! !{speed}!')
ValueError: Скорость не может быть отрицательной! !-5!