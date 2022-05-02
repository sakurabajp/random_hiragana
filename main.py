import random
import time

time1 = time.time()
Number = 0

while time1 != -1:
    time.sleep(0.001)
    with open('hiragana.txt', 'r', encoding="utf-8") as f:
        Number = Number + 1
        random1 = f.read().split("\n")
        print(random.choice(random1),random.choice(random1),random.choice(random1))
        print(int(Number),('回目'))
