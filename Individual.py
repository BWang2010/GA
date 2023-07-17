import string
import random
class Individual:
    def __init__(self,target):
        self.target = target
        self.genetics = self.rand_genetics()

    def rand_genetics(self):
        num = len(self.target)
        for x in range(num):
            randomLetter = random.choice(string.ascii_lowercase)
            print(randomLetter)
