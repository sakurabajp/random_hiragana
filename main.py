import random
import time

time1 = time.time()
Number = 0

while time1 != -1:
    time.sleep(1)
    with open('ひらがな.txt', 'r', encoding="utf-8") as f:
        Number = Number + 1
        kw_list = f.read().split("\n")
        random1 = kw_list
        print(random.choice(random1),random.choice(random1),random.choice(random1))
        print(int(Number),('回目'))
