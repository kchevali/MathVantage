import pyautogui
import xerox
from time import sleep, time

holdTime = 0.01
pyautogui.PAUSE = 0.05


def countDown():
    print("Countdown")
    for i in range(5):
        print(5 - i)
        sleep(1)


def getInput():
    print("Enter numbers (include ', ' - except the last one)")
    return [int(x) for x in input().split(", ")]


def copy():
    pyautogui.hotkey('command', 'c', interval=holdTime)
    return xerox.paste()


def highlightDown():
    pyautogui.hotkey('shift', 'down', interval=holdTime)


def highlightRight():
    pyautogui.hotkey('shift', 'right', interval=holdTime)


def highlightUp():
    pyautogui.hotkey('shift', 'up', interval=holdTime)


def moveUp():
    pyautogui.press('up')
    moveToStart()


def moveDown():
    moveToEnd()
    pyautogui.press('right')


def moveToStart():
    pyautogui.hotkey('ctrl', 'a', interval=holdTime)


def moveToEnd():
    pyautogui.hotkey('ctrl', 'e', interval=holdTime)


def getLines():
    moveToStart()
    highlightDown()
    lines = copy()
    # pyautogui.press('left')
    return lines.split("\n")


def checkNum(line):
    parts = line.split(". ")
    if len(parts) == 0:
        return None
    try:
        return int(parts[0])
    except:
        pass
    return None


def getNum(lines):
    # print(lines)
    for i in range(-1, -len(lines) - 1, -1):
        num = checkNum(lines[i])
        if num != None:
            return num
    return None


def goToNumAbove(nextNum):
    num = None
    while num == None or num <= nextNum:
        lines = getLines()
        moveDown()
        num = getNum(lines)
    moveUp()


def deleteUpTo(nextNum, index):
    num = None
    while num != nextNum:
        lines = getLines()
        num = getNum(lines)
        if num != nextNum:
            delete()
    highlightUp()

    replaceNumber(nextNum, index)
    moveDown()


def delete():
    pyautogui.press('del')


def write(string):
    pyautogui.write(string)


def replaceNumber(old, new):
    moveToStart()
    for i in range(len(str(old))):
        highlightRight()
    write(str(new))
    moveDown()


if __name__ == '__main__':
    maxQuestion = 125

    # nums = getInput()
    nums = [2, 10, 13, 17, 21, 29, 32, 38, 44, 47, 55, 56, 63,
            68, 71, 76, 85, 86, 94, 100, 102, 110, 111, 117, 121]
    countDown()
    print("Start")
    startTime = time()
    index = 1
    for num in nums:
        print("Going to Question:", num)
        deleteUpTo(num, index)
        if(num < maxQuestion):
            goToNumAbove(num)
        index += 1
    print("Done:", round((time() - startTime) / 60, 2), "min")

    # replaceNumber(1, 555)
