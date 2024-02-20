import random, pyautogui, time

while True:
    x = random.randint(1, 1000)
    y = random.randint(1, 1200)
    pyautogui.moveTo(x,y, 2)
    time.sleep(200)
