import random 
r = random.randint(1, 100)
while True:
    num = input('請猜一到一百的整數: ')
    num = int(num)
    if num == r: 
        print('終於猜對了')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')