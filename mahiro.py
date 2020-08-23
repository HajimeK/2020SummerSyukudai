# Add your Python code here. E.g.
from microbit import *

display.scroll('Mahiro 2020')
#display.show(Image.FABULOUS)fds

on = 1
off = 0

def one(a):
    pin0.write_digital(a)

def two(a):
    pin1.write_digital(a)

def three(a):
    pin2.write_digital(a)

# 0.5秒待つ
def wait_500():
    sleep(500)

# 10秒待つ
def wait_10000():
    sleep(10000)

while True: #永遠に繰り返す
    for i in range(3): # 3回くりかえす
        one(on)
        wait_500()
        two(on)
        wait_500()
        three(on)

    # 全部けす
    one(off)
    two(off)
    three(off)
    
    for i in range(5): # ５回くりかえす
        one(on)
        wait_500()
        one(off)
        two(on)
        wait_500
        three(on)
        wait_500()
        three(off)

    # 全部つける
    one(on)
    two(on)
    three(on)
    wait_10000()
    # 全部けす
    one(off)
    two(off)
    three(off)



