import random, pyautogui, time

while True:
    x = random.randint(1, 1928)
    y = random.randint(1, 1888)
    pyautogui.moveTo(x,y, 2)
    time.sleep(200)
