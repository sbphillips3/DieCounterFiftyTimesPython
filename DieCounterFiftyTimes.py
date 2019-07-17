import random
from collections import Counter

numbersOnDie = [random.randrange(1, 7) for i in range(50)]

counter = Counter(numbersOnDie)

for value, count in sorted(counter.items()):
    print(f'{value:<5}{count}')

