import pyautogui
from time import sleep

def Prepare():
    pyautogui.click(342, 97)
    sleep(0.1)

    pyautogui.click(1126,91)
    sleep(0.1)

    pyautogui.click(612, 499)
    sleep(0.1)

    pyautogui.click(449, 109)
    sleep(0.1)

    pyautogui.click(910, 91)
    sleep(0.1)



def H():

    pyautogui.moveTo(159, 265)
    sleep(0.1)

    pyautogui.dragRel(0, 160)
    sleep(0.1)

    pyautogui.dragRel(0, -80)
    sleep(0.1)

    pyautogui.dragRel(80, 0)
    sleep(0.1)

    pyautogui.dragRel(0, -80)
    sleep(0.1)

    pyautogui.dragRel(0, 160)
    sleep(0.1)

def I():
    pyautogui.moveTo(295, 265)
    sleep(0.1)

    pyautogui.dragRel(0, 160)
    sleep(0.1)

def R():
    pyautogui.moveTo(350, 265)
    sleep(0.1)

    pyautogui.dragRel(0, 160)
    sleep(0.1)

    pyautogui.moveTo(350, 265)
    sleep(0.1)

    pyautogui.dragRel(84, 41)
    sleep(0.1)

    pyautogui.dragRel(-84, 41)
    sleep(0.1)

    pyautogui.dragRel(103, 77)
    sleep(0.1)

def E():
    pyautogui.moveTo(500, 265)
    sleep(0.1)

    pyautogui.dragRel(0, 160)
    sleep(0.1)

    pyautogui.moveTo(500, 265)
    sleep(0.1)

    pyautogui.dragRel(90, 0)
    sleep(0.1)

    pyautogui.moveTo(500, 265)
    sleep(0.1)

    pyautogui.dragRel(0, 80)
    sleep(0.1)

    pyautogui.dragRel(90, 0)
    sleep(0.1)

    pyautogui.dragRel(-90, 0)
    sleep(0.1)

    pyautogui.dragRel(0, 80)
    sleep(0.1)

    pyautogui.dragRel(90, 0)
    sleep(0.1)

def M():
    pyautogui.moveTo(437, 500)
    sleep(0.1)

    pyautogui.dragRel(0, 160)
    sleep(0.1)

    pyautogui.moveTo(437, 500)
    sleep(0.1)

    pyautogui.dragRel(71, 90)
    sleep(0.1)

    pyautogui.dragRel(71, -90)
    sleep(0.1)

    pyautogui.dragRel(0, 160)
    sleep(0.1)

def E2():
    pyautogui.moveTo(650, 500)
    sleep(0.1)

    pyautogui.dragRel(0, 160)
    sleep(0.1)

    pyautogui.moveTo(650, 500)
    sleep(0.1)

    pyautogui.dragRel(90, 0)
    sleep(0.1)

    pyautogui.moveTo(650, 500)
    sleep(0.1)

    pyautogui.dragRel(0, 80)
    sleep(0.1)

    pyautogui.dragRel(90, 0)
    sleep(0.1)

    pyautogui.dragRel(-90, 0)
    sleep(0.1)

    pyautogui.dragRel(0, 80)
    sleep(0.1)

    pyautogui.dragRel(90, 0)
    sleep(0.1)


def Assinatura():
    pyautogui.click(385, 94)
    sleep(0.1)

    pyautogui.click(818, 729)
    sleep(0.1)

    pyautogui.write("Ass. Marco Branco")
    sleep(0.1)
    pyautogui.press("ENTER")
    pyautogui.press("ENTER")
    sleep(0.1)
    pyautogui.write("Ps. Não sou um robo")


Prepare()

H()
I()
R()
E()

M()
E2()

Assinatura()