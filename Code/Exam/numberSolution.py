import pyautogui
import xerox
from time import sleep, time
import subprocess

pulsePause = 0.01
miniPause = 0.05
shortPause = 0.1
longPause = 0.5
extraLongPause = 1

quitPause = 2
highlightPause = 0.05
searchPause = 1

debugPause = 4
# pya8. utogui.PAUSE = 0.05
pyautogui.PAUSE = 0.05


sections = ["1BasicConcepts", "2Functions", "3Trigonometry",
            "4Limits", "5Derivatives", "6Integrals"]
sectionNames = ["Basic Concepts", "Functions",
                "Trigonometry", "Limits", "Derivatives", "Integrals"]
lessons = [
    [(1, 3), (1, 6), (1, 9)],
    [(10, 12), (10, 15), (10, 19)],
    [(20, 22), (20, 26)],
    [(27, 29), (27, 31)],
    [(32, 34), (32, 37)],
    [(38, 40), (38, 42)]
]

totalQ = [125, 125, 125, 125, 115, 125]

directoryPath = "/Users/kevin/Documents/Repos/MathVantage/Exams"


def openFile(path):
    subprocess.run(['open', path], check=True)
    sleep(2)


def fullScreen():
    pyautogui.hotkey('command', 'ctrl', 'f', interval=longPause)


def countDown():
    print("Countdown")
    for i in range(5):
        print(5 - i)
        sleep(1)


def copy():
    pyautogui.hotkey('command', 'c', interval=shortPause)
    line = xerox.paste()
    return line


def highlightDown():
    pyautogui.hotkey('shift', 'down', interval=highlightPause)


def highlightRight():
    pyautogui.hotkey('shift', 'right', interval=highlightPause)


def highlightUp():
    pyautogui.hotkey('shift', 'up', interval=highlightPause)


def moveDown():
    moveToEnd()
    pyautogui.press('right', interval=pulsePause)


def moveToStart():
    pyautogui.hotkey('ctrl', 'a', interval=pulsePause)


def moveToEnd():
    pyautogui.hotkey('ctrl', 'e', interval=pulsePause)


def gotoStartPage():
    pyautogui.hotkey('command', 'up', interval=pulsePause)


def write(string):
    pyautogui.write(string)
    sleep(0.4)


def click(pos):
    pyautogui.click(pos[0], pos[1], interval=pulsePause)


def quitPages():
    pyautogui.hotkey('command', 'q', interval=quitPause)


def openBook(numBook, numExam):
    section = sections[numBook - 1]
    sectionName = sectionNames[numBook - 1]
    basePath = "{}/{}/".format(directoryPath, section)

    templateFileName = "{} - Exam {} - Template.pages".format(
        sectionName, numExam)
    templatePath = basePath + templateFileName
    openFile(templatePath)
    fullScreen()


def setTextColor():
    colorBoxPos = (1225, 395)
    whitePos = (1055, 518)
    click(colorBoxPos)
    click(whitePos)
    moveDown()


def handleBook(numBook, index):
    if index == 1:
        gotoStartPage()
    nextDownCounter = 0
    downCounter = 3
    print("Initial Skipping by:", downCounter)
    while index <= totalQ[numBook - 1]:
        if index % 5 == 2:
            nextDownCounter += 1
        moveToStart()
        highlightDown()
        found = copy().lower()
        isSolution = "solution:" in found or "solutions:" in found
        if isSolution:
            moveToStart()
            write("{:03}".format(index))
            highlightUp()
            highlightRight()
            setTextColor()
            index += 1
            if index % 5 == 1:
                downCounter = 3
                # print("Safe Skipping by:", downCounter)
            if index % 5 == 2:
                nextDownCounter = 0
            elif index % 5 == 3:
                downCounter = nextDownCounter
                # print("Actual Skipping by:", downCounter)
        moveToStart()
        for i in range(downCounter if isSolution else 1):
            moveDown()


if __name__ == '__main__':
    countDown()
    print("Start")
    startTime = time()
    books = [1, 2, 3, 4, 5, 6]

    startBook = 6
    startExam = 2
    startQ = 83
    try:
        for numBook in books:
            if numBook < startBook:
                continue
            examCount = len(lessons[numBook - 1])
            for numExam in range(1, 1 + examCount):
                if numBook == startBook and numExam < startExam:
                    continue
                q = startQ if numBook == startBook and numExam == startExam else 1
                print("Start Book:", numBook, "Exam:",
                      numExam, "Start Question:", q)
                if q == 1:
                    openBook(numBook, numExam)
                handleBook(numBook, q)
                quitPages()
    except:
        pass
    print("Done:", round((time() - startTime) / 60, 2), "min")

    # replaceNumber(1, 555)
