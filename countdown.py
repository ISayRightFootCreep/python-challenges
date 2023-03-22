import time
a = int(input('how long to count down? '))
for i in range(a, 0, -1):
    print(i)
    time.sleep(1)
print('lift off!')
