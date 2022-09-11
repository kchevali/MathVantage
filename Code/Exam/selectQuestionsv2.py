import pyautogui
from time import sleep, time
import shutil
import subprocess
import xerox
import os
import traceback
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key

pulsePause = 0.01
shortPause = 0.1
longPause = 0.5
extraLongPause = 1

quitPause = 5
highlightPause = 0.05
searchPause = 2.5

debugPause = 4

endSectionQuestionSpace = 20
maxQ = 200
finalSectionQ = 21
displaySections = ["Basic Concepts", "Functions", "Trigonometry",
                   "Limits", "Derivatives", "Integrals", "Plane Geometry", "Solid Geometry", "Analytic Geometry"]
fileSections = ["Basic_Concepts", "Functions", "Trigonometry",
                "Limits", "Derivatives", "Integrals", "Plane_Geometry", "Solid_Geometry", "Analytic_Geometry"]
lessons = [
    [(1, 3), (4, 6), (7, 9)],
    [(10, 12), (13, 15), (16, 19)],
    [(20, 22), (23, 26)],
    [(27, 29), (30, 31)],
    [(32, 34), (35, 37)],
    [(38, 40), (41, 42)],
    [(43, 46), (47, 49), (50, 51)],
    [(52, 54), (55, 57), (58, 59)],
    [(60, 63), (64, 66)]
]

totalQ = [
    [125, 125, 125],
    [125, 125, 125],
    [125, 125],
    [125, 125],
    [125, 115],
    [125, 125],
    [125, 125, 125],
    [125, 125, 125],
    [125, 125]
]

examQ = [
    [25, 25, 25],
    [25, 25, 25],
    [25, 25],
    [25, 25],
    [25, 23],
    [25, 25],
    [25, 25, 25],
    [25, 25, 25],
    [25, 25]
]
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

directoryPath = "/Users/kevin/Documents/Repos/MathVantage/Exams"

shiftKeys = [
    (':', ';')
]

# pynput
keyDict = {}
for key in Key:
    keyDict[key.name] = key


def getInputLines():
    f = open("questions.txt", "r")
    out = []
    for line in f.readlines():
        line = line.split(": ")
        if len(line) > 1:
            arr = []
            for x in line[1].split(", "):
                try:
                    num = int(x)
                    arr.append(num)
                except:
                    pass
            out.append(arr)
    return out


def countDown():
    print("Countdown")
    for i in range(5):
        print(5 - i)
        sleep(1)


def wait(msg=None, cond=True):
    if cond:
        if msg != None:
            print(msg)
        input()
        countDown()


def pause(msg=None, cond=True):
    if cond:
        if msg != None:
            print(msg)
        sleep(2)


# def write(string):
#     """
#     Keys that require the shift to be pressed such as ':' needs to be explicitly typed as 'shift' + ';'
#     """
#     for ch, base in shiftKeys:
#         if ch in string:
#             parts = string.split(ch)
#             for i in range(len(parts)):
#                 write(parts[i])
#                 if i + 1 < len(parts):
#                     keyUp('shift')
#                     print("PRESS", base)
#                     keyPress(base, interval=pulsePause)
#                     keyDown('shift')
#             return
#     typeString(string)

# File Operations.


def copyFile(src, dest):
    shutil.copy2(src, dest)
    sleep(2)


def openFile(path):
    subprocess.run(['open', path], check=True)
    sleep(2)


def deleteFile(path):
    try:
        os.remove(path)
    except:
        pass

# Input Operations


def keyPress(*args, interval=0):
    for key in args:
        if len(key) > 1:
            key = keyDict[key]
        keyboard.press(key)

    for key in reversed(args):
        if len(key) > 1:
            key = keyDict[key]
        keyboard.release(key)


def write(string):
    keyboard.type(string)


def getClipboard():
    return xerox.paste()


def moveMouseTo(pos):
    pyautogui.moveTo(pos)


def click(pos, count=1):
    for i in range(count):
        moveMouseTo(pos)
        mouse.click(Button.left)

# My Operations


def fullScreen():
    keyPress('cmd', 'ctrl', 'f')
    sleep(extraLongPause)


def searchBar():
    keyPress('cmd', 'f', interval=shortPause)


def escape():
    keyPress('esc', interval=pulsePause)


def enter():
    keyPress('enter', interval=pulsePause)


def gotoQuestion(numQ, index):
    search(str(numQ) + ". ")
    if index != None:
        write("\n" + str(index) + ". ")
    moveRight()
    moveToStartOfLine()


def search(s, depth=0, terminateOnFail=True):
    searchBar()
    write("\\n" + s)
    sleep(searchPause)
    escape()

    current = copy()
    if(current != ("\n" + s)):
        if(depth < 2):
            return search(s, depth + 1, terminateOnFail)
        elif terminateOnFail:
            print("Cannot find:", s)
            # print("Found:'" + current + "'")
            exit()
        else:
            return False
    return True


def gotoStartPage():
    keyPress('cmd', 'up', interval=pulsePause)


def gotoEndPage():
    keyPress('cmd', 'down', interval=pulsePause)


def highlightAbove():
    keyPress('cmd', 'shift', 'up', interval=highlightPause)


def deleteAbove(cursorDown=False):
    highlightAbove()
    if cursorDown:
        highlightDown()
    delete()


def cutAbove(cursorDown=False):
    highlightAbove()
    if cursorDown:
        highlightDown()
    cut()


def copyAbove():
    highlightAbove()
    copy()


def highlightBelow():
    keyPress('cmd', 'shift', 'down', interval=highlightPause)


def deleteBelow():
    highlightBelow()
    delete()


def cutBelow():
    highlightBelow()
    cut()


def swapWindows():
    keyPress('ctrl', 'tab', interval=shortPause)


def cut():
    keyPress('cmd', 'x', interval=shortPause)


def save():
    keyPress('cmd', 's', interval=shortPause)


def fast_copy():
    keyPress('cmd', 'c', interval=shortPause)


def copy():
    keyPress('cmd', 'c', interval=shortPause)
    sleep(0.75)
    line = getClipboard()
    sleep(0.01)
    return line


def paste():
    keyPress('cmd', 'v', interval=shortPause)


def highlightDown():
    keyPress('shift', 'down', interval=highlightPause)


def highlightRight():
    keyPress('shift', 'right', interval=highlightPause)


def highlightUp():
    keyPress('shift', 'up', interval=highlightPause)


def moveDown():
    keyPress('down', interval=pulsePause)

def moveUp():
    keyPress('up', interval=pulsePause)


def movePageDown():
    keyPress('ctrl', 'v', interval=pulsePause)


def moveToStartOfLine():
    keyPress('ctrl', 'a', interval=pulsePause)


def moveRight():
    keyPress('right', interval=pulsePause)


def moveToEnd():
    keyPress('ctrl', 'e', interval=pulsePause)


def delete():
    keyPress('ctrl', 'h', interval=pulsePause)


def printPages():
    keyPress('cmd', 'p', interval=longPause)


def closeAllWindows(count=2):
    for i in range(count):
        keyPress('cmd', 'w')
        sleep(quitPause)


def quitPages():
    closeAllWindows()


def hoverMouse(pos):
    pyautogui.moveTo(pos)
    sleep(extraLongPause)

# Page Operations


def setupFirstPage(numBook, numExam, numQ):
    sectionName = displaySections[numBook - 1]
    middleHeaderPos = (520, 115)
    rightHeaderPos = (730, 115)

    y = 225

    titlePos = (370, y)
    lessonPos = (575, y)
    textPos = (215, y)
    title = "{} - Exam {}".format(sectionName, numExam)
    lessonStart, lessonEnd = lessons[numBook - 1][numExam - 1]

    # Write middle header title.
    click(middleHeaderPos, count=2)
    write(title)

    # Write right header title.
    click(rightHeaderPos)
    write("Exam Number: {:03}".format(numQ))

    # Write main title.
    click(titlePos)
    write(title)
    click(lessonPos)
    write("Lesson: {}-{}".format(lessonStart, lessonEnd))
    click(textPos)
    moveRight()
    # pause("Check for cursor")

    sleep(2)
    save()
    sleep(2)
    createQuestionFile(numBook, numExam, numQ)

    swapWindows()


def adjustFinalPage():
    finalPagePos = (400, 680)
    textWrapPos = (1140, 215)
    nonePos = (1140, 245)
    textPos = (620, 730)
    stayOnPagePos = (1100, 155)

    sleep(0.5)
    gotoEndPage()
    click(finalPagePos)
    sleep(0.05)

    click(textWrapPos)
    sleep(0.5)
    click(nonePos)
    sleep(0.5)
    click(stayOnPagePos)
    click(textPos)


def columnBreak():
    pPos = (380, 20)
    columnPos = (420, 110)

    click(pPos)
    sleep(0.5)
    click(columnPos)


def clearPDF(numBook, numExam, numQ):
    section = fileSections[numBook - 1]
    basePath = "{}/{}/{}PDF/".format(directoryPath, section, section)

    solutionPDFFileName = "{} - Exam {} - {:03d} Solution.pages.pdf".format(
        section, numExam, numQ)
    questionPDFFileName = "{} - Exam {} - {:03d} Questions.pages.pdf".format(
        section, numExam, numQ)

    solutionPath = basePath + solutionPDFFileName
    questionPath = basePath + questionPDFFileName

    deleteFile(solutionPath)
    deleteFile(questionPath)


def convertToPDF(numBook):
    pdfPos = (470, 555)
    savePos = (510, 600)
    belowFolderPos = (500, 300)
    section = fileSections[numBook - 1]

    printPages()
    # print("CLICK PDF")
    # sleep(1)
    click(pdfPos)
    # print("CLICK SAVE")
    # sleep(1)
    click(savePos)

    sleep(2)
    searchBar()
    write(section + "PDF")
    sleep(extraLongPause)
    click(belowFolderPos)
    moveDown()
    enter()
    sleep(2)


def createFiles(numBook, numExam, numQ):
    section = fileSections[numBook - 1]
    basePath = "{}/{}/".format(directoryPath, section)
    pagesPath = basePath + "Pages/"

    builderFileName = "ExamBuilder.pages"
    srcFileName = "Source.pages"
    templateFileName = "{} - Exam {} - Template.pages".format(
        section, numExam)
    solutionFileName = "{} - Exam {} - {:03d} Solution.pages".format(
        section, numExam, numQ)

    builderPath = "{}/{}".format(directoryPath, builderFileName)
    solutionPath = pagesPath + solutionFileName

    templatePath = basePath + templateFileName
    srcPath = pagesPath + srcFileName

    # Have to delete Source.pages first to prevent errors later when closing it
    deleteFile(srcPath)
    copyFile(templatePath, srcPath)
    openFile(srcPath)
    fullScreen()

    copyFile(builderPath, solutionPath)
    openFile(solutionPath)


def createQuestionFile(numBook, numExam, numQ):
    section = fileSections[numBook - 1]
    basePath = "{}/{}/".format(directoryPath, section)
    pagesPath = basePath + "Pages/"

    solutionFileName = "{} - Exam {} - {:03d} Solution.pages".format(
        section, numExam, numQ)
    questionFileName = "{} - Exam {} - {:03d} Questions.pages".format(
        section, numExam, numQ)

    solutionPath = pagesPath + solutionFileName
    questionPath = pagesPath + questionFileName

    copyFile(solutionPath, questionPath)


def openQuestionFiles(numBook, numExam, numQ):
    section = fileSections[numBook - 1]
    basePath = "{}/{}/".format(directoryPath, section)
    pagesPath = basePath + "Pages/"

    srcFileName = "Source.pages"
    solutionFileName = "{} - Exam {} - {:03d} Solution.pages".format(
        section, numExam, numQ)
    questionFileName = "{} - Exam {} - {:03d} Questions.pages".format(
        section, numExam, numQ)

    srcPath = pagesPath + srcFileName
    solutionPath = pagesPath + solutionFileName
    questionPath = pagesPath + questionFileName

    copyFile(solutionPath, srcPath)
    openFile(questionPath)
    fullScreen()
    openFile(srcPath)


# building the first document (q + sol)
def processFiles(nums, numBook, numExam, convertPDF, quitAtEnd=True):
    index = 1
    prevNum = 0
    gotoStartPage()
    for num in nums:
        if(num > totalQ[numBook - 1][numExam - 1]):
            break

        print(num, end=" " if(index % 5) > 0 else "\n")
        if(num == prevNum + 1):
            enter()
            gotoStartPage()

        gotoQuestion(num, index)
        deleteAbove(cursorDown=False)
        if num < totalQ[numBook - 1][numExam - 1]:
            gotoQuestion(num + 1, None)
        else:
            gotoEndPage()
        sleep(1)
        cutAbove(cursorDown=False)
        swapWindows()
        if(index == finalSectionQ):
            pause("GO FOR ADJUST")
            adjustFinalPage()
            # wait(msg="Did final file")
        paste()
        # if(index == 5):
        #     return
        swapWindows()
        index += 1
        prevNum = num

    if convertPDF:
        swapWindows()
        convertToPDF(numBook)
    if quitAtEnd:
        quitPages()
    sleep(2)
    print("\n")

# building the second document (q only)


def processQuestionFiles(numBook, numExam, nums, convertPDF, quitAtEnd=True):
    # textPos = (180, 225)
    # click(textPos)
    gotoStartPage()
    swapWindows()
    # for i in range(10):
    sleep(1)
    click((250, 20))
    sleep(1)
    click((212,222), count=2)
    moveDown() #some reason this moves 2 pages down
    moveUp() # 1 page back up
    swapWindows()
    maxNumQ = examQ[numBook - 1][numExam - 1]
    for index in range(1, 1 + maxNumQ):  # [1,25]
        # wait(index == 23, "At 23!")
        numQ = nums[index - 1]  # [1,125]
        search("{:03}Solution".format(numQ))
        moveToStartOfLine()
        highlightAbove()
        highlightRight()
        copy()
        # wait(index == 24 or index == 23, "COPIED")
        swapWindows()
        pause("Go to start page of Question", cond=index == 1)
        if(index == finalSectionQ):
            adjustFinalPage()
        if (index == 23 or index == 25):
            sleep(0.5)
            columnBreak()
        paste()
        # wait(index == 24 or index == 23, "PASTED")
        if(index == 21 or index == 23):
            for i in range(endSectionQuestionSpace):
                enter()

        swapWindows()
        if index < maxNumQ:
            search(str(index + 1) + ". ")
            moveToStartOfLine()
            highlightAbove()
            highlightRight()
            delete()
    if convertPDF:
        swapWindows()
        convertToPDF(numBook)
    if quitAtEnd:
        quitPages()


def getExamArray(startQ, count):
    index = 1
    q = 1
    endQ = startQ + count
    for bookIndex in range(len(fileSections)):
        for examIndex in range(len(lessons[bookIndex])):

            # do not change repeat! Will have to reset
            for i in range(10):
                if q >= endQ:
                    break

                if q >= startQ:
                    yield (index, q % maxQ, bookIndex + 1, examIndex + 1)
                    index += 1
                q += 1


def startUp():
    print("Quitting")
    closeAllWindows()
    print("Deleting")
    base = "/Users/kevin/Documents/Repos/MathVantage/Exams/Basic_Concepts/Pages/"
    deleteFile(base + "Basic_Concepts - Exam 2 - 011 Questions.pages")
    deleteFile(base + "Basic_Concepts - Exam 2 - 011 Solution.pages")
    deleteFile(base + "Source.pages")
    print("Done")
    sleep(2)


if __name__ == '__main__':
    convertPDF = False
    quitAtEnd = True
    nums = getInputLines()

    startQ = 168
    qCount = 3

    countDown()
    startTime = time()

    try:
        for (index, numQ, numBook, numExam) in getExamArray(startQ, qCount):
            print(str(index) + ". Starting Book:", numBook, "Exam:", numExam, "v:", numQ)
            createFiles(numBook, numExam, numQ)
            setupFirstPage(numBook, numExam, numQ)
            if convertPDF:
                clearPDF(numBook, numExam, numQ)
            processFiles(nums[numQ - 1], numBook, numExam, convertPDF)
            openQuestionFiles(numBook, numExam, numQ)
            processQuestionFiles(numBook, numExam, nums[numQ - 1], convertPDF, quitAtEnd=quitAtEnd)

    except Exception as error:
        print("Terminate with Error:", error)
        print("Stack:", traceback.format_exc())

    print("Done:", round((time() - startTime) / 60, 2), "min")
