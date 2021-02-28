import pynput
from time import sleep, time
import shutil
import subprocess
import xerox
import os
import traceback


finalSectionQ = 21
sections = ["1BasicConcepts", "2Functions", "3Trigonometry",
            "4Limits", "5Derivatives", "6Integrals", "7PlaneGeometry"]
sectionNames = ["Basic Concepts", "Functions",
                "Trigonometry", "Limits", "Derivatives", "Integrals", "PlaneGeometry"]
lessons = [
    [(1, 3), (1, 6), (1, 9)],
    [(10, 12), (10, 15), (10, 19)],
    [(20, 22), (20, 26)],
    [(27, 29), (27, 31)],
    [(32, 34), (32, 37)],
    [(38, 40), (38, 42)],
    [(43, 46), (43, 49), (43, 52)]
]

totalQ = [
    [125, 125, 125],
    [125, 125, 125],
    [125, 125],
    [125, 125],
    [125, 115],
    [125, 125],
    [125, 125, 125]
]

examQ = [
    [25, 25, 25],
    [25, 25, 25],
    [25, 25],
    [25, 25],
    [25, 23],
    [25, 25],
    [25, 25, 25]
]

directoryPath = "/Users/kevin/Documents/Repos/MathVantage/Exams"


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


# def sleep(value):
#     if pressNextMode:

#     else:
#         sleep(value)


def copyFile(src, dest):
    shutil.copy2(src, dest)
    sleep(1)


def openFile(path):
    subprocess.run(['open', path], check=True)
    sleep(2)


def deleteFile(path):
    try:
        os.remove(path)
    except:
        pass


def fullScreen():
    pyautogui.hotkey('command', 'ctrl', 'f', interval=longPause)


def searchBar():
    pyautogui.hotkey('command', 'f', interval=shortPause)


def escape():
    pyautogui.press('esc', interval=pulsePause)


def enter():
    pyautogui.press('enter', interval=pulsePause)


def gotoQuestion(numQ, index):
    search(str(numQ) + ". ")
    if index != None:
        write("\n" + str(index) + ". ")
    moveRight()
    moveToStart()


def search(s, depth=0):
    searchBar()
    write("\\n" + s)
    sleep(searchPause)
    escape()

    current = copy()
    if(current != ("\n" + s)):
        if(depth < 2):
            search(s, depth + 1)
        else:
            print("Cannot find:", s)
            # print("Found:'" + current + "'")
            exit()


def gotoStartPage():
    pyautogui.hotkey('command', 'up', interval=pulsePause)


def gotoEndPage():
    pyautogui.hotkey('command', 'down', interval=pulsePause)


def highlightAbove():
    pyautogui.hotkey('command', 'shift', 'up', interval=highlightPause)


def deleteAbove():
    highlightAbove()
    delete()


def cutAbove():
    highlightAbove()
    cut()


def copyAbove():
    highlightAbove()
    copy()


def highlightBelow():
    pyautogui.hotkey('command', 'shift', 'down', interval=highlightPause)


def deleteBelow():
    highlightBelow()
    delete()


def cutBelow():
    highlightBelow()
    cut()


def swapWindows():
    pyautogui.hotkey('ctrl', 'tab', interval=shortPause)


def cut():
    pyautogui.hotkey('command', 'x', interval=shortPause)


def save():
    pyautogui.hotkey('command', 's', interval=shortPause)


def fast_copy():
    pyautogui.hotkey('command', 'c', interval=shortPause)


def copy():
    pyautogui.hotkey('command', 'c', interval=shortPause)
    sleep(0.75)
    line = xerox.paste()
    sleep(0.01)
    return line


def paste():
    pyautogui.hotkey('command', 'v', interval=shortPause)


def highlightDown():
    pyautogui.hotkey('shift', 'down', interval=highlightPause)


def highlightRight():
    pyautogui.hotkey('shift', 'right', interval=highlightPause)


def highlightUp():
    pyautogui.hotkey('shift', 'up', interval=highlightPause)


def moveDown():
    pyautogui.press('down', interval=pulsePause)


def moveToStart():
    pyautogui.hotkey('ctrl', 'a', interval=pulsePause)


def moveRight():
    pyautogui.press('right', interval=pulsePause)


def moveToEnd():
    pyautogui.hotkey('ctrl', 'e', interval=pulsePause)


def delete():
    pyautogui.hotkey('ctrl', 'h', interval=pulsePause)


def printPages():
    pyautogui.hotkey('command', 'p', interval=longPause)


def quitPages():
    pyautogui.hotkey('command', 'q', interval=quitPause)


def write(string):
    pyautogui.write(string)


def click(pos):
    pyautogui.click(pos[0], pos[1], interval=pulsePause)


def hoverMouse(pos):
    pyautogui.moveTo(pos)
    sleep(extraLongPause)


def setupFirstPage(numBook, numExam, numQ):
    sectionName = sectionNames[numBook - 1]
    rightHeaderPos = (730, 110)

    y = 225
    titlePos = (370, y)
    lessonPos = (575, y)
    textPos = (180, y)
    title = "{} - Exam {}".format(sectionName, numExam)
    lessonStart, lessonEnd = lessons[numBook - 1][numExam - 1]

    write(title)
    click(rightHeaderPos)
    write("Exam Number: {:03}".format(numQ))
    click(titlePos)
    write(title)
    click(lessonPos)
    write("Lesson: {}-{}".format(lessonStart, lessonEnd))
    click(textPos)
    moveRight()

    sleep(2)
    save()
    sleep(1)
    createLectureFile(numBook, numExam, numQ)

    swapWindows()


def adjustFinalPage():
    finalPagePos = (400, 680)
    textWrapPos = (1140, 215)
    nonePos = (1140, 245)
    textPos = (620, 730)
    stayOnPagePos = (1100, 155)

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
    columnPos = (420, 100)

    click(pPos)
    click(columnPos)


def clearPDF(numBook, numExam, numQ):
    section = sections[numBook - 1]
    sectionName = sectionNames[numBook - 1]
    basePath = "{}/{}/{}PDF/".format(directoryPath, section, section)

    solutionPDFFileName = "{} - Exam {} - {:03d} Solution.pages.pdf".format(
        sectionName, numExam, numQ)
    lecturePDFFileName = "{} - Exam {} - {:03d}.pages.pdf".format(
        sectionName, numExam, numQ)

    solutionPath = basePath + solutionPDFFileName
    lecturePath = basePath + lecturePDFFileName

    deleteFile(solutionPath)
    deleteFile(lecturePath)


def convertToPDF(numBook):
    pdfPos = (470, 555)
    savePos = (510, 600)
    belowFolderPos = (500, 300)
    section = sections[numBook - 1]

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
    section = sections[numBook - 1]
    sectionName = sectionNames[numBook - 1]
    basePath = "{}/{}/".format(directoryPath, section)
    pagesPath = basePath + "Pages/"

    builderFileName = "ExamBuilder.pages"
    srcFileName = "Source.pages"
    templateFileName = "{} - Exam {} - Template.pages".format(
        sectionName, numExam)
    solutionFileName = "{} - Exam {} - {:03d} Solution.pages".format(
        sectionName, numExam, numQ)

    builderPath = "{}/{}".format(directoryPath, builderFileName)
    solutionPath = pagesPath + solutionFileName

    templatePath = basePath + templateFileName
    srcPath = pagesPath + srcFileName

    copyFile(templatePath, srcPath)
    openFile(srcPath)
    fullScreen()

    copyFile(builderPath, solutionPath)
    openFile(solutionPath)


def createLectureFile(numBook, numExam, numQ):
    section = sections[numBook - 1]
    sectionName = sectionNames[numBook - 1]
    basePath = "{}/{}/".format(directoryPath, section)
    pagesPath = basePath + "Pages/"

    solutionFileName = "{} - Exam {} - {:03d} Solution.pages".format(
        sectionName, numExam, numQ)
    lectureFileName = "{} - Exam {} - {:03d}.pages".format(
        sectionName, numExam, numQ)

    solutionPath = pagesPath + solutionFileName
    lecturePath = pagesPath + lectureFileName

    copyFile(solutionPath, lecturePath)


def openLectureFiles(numBook, numExam, numQ):
    section = sections[numBook - 1]
    sectionName = sectionNames[numBook - 1]
    basePath = "{}/{}/".format(directoryPath, section)
    pagesPath = basePath + "Pages/"

    srcFileName = "Source.pages"
    solutionFileName = "{} - Exam {} - {:03d} Solution.pages".format(
        sectionName, numExam, numQ)
    lectureFileName = "{} - Exam {} - {:03d}.pages".format(
        sectionName, numExam, numQ)

    srcPath = pagesPath + srcFileName
    solutionPath = pagesPath + solutionFileName
    lecturePath = pagesPath + lectureFileName

    copyFile(solutionPath, srcPath)
    openFile(lecturePath)
    fullScreen()
    openFile(srcPath)


def processFiles(nums, numBook, numExam, convertPDF):
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
        deleteAbove()
        if num < totalQ[numBook - 1][numExam - 1]:
            gotoQuestion(num + 1, None)
        else:
            gotoEndPage()

        cutAbove()
        swapWindows()
        if(index == finalSectionQ):
            adjustFinalPage()
        paste()
        # if(index == 5):
        #     return
        swapWindows()
        index += 1
        prevNum = num

    if convertPDF:
        swapWindows()
        convertToPDF(numBook)
    quitPages()

    print("\n")


def processLectureFiles(numBook, numExam, nums, convertPDF):
    # textPos = (180, 225)
    # click(textPos)
    gotoStartPage()
    maxNumQ = examQ[numBook - 1][numExam - 1]
    for index in range(1, 1 + maxNumQ):
        numQ = nums[index - 1]
        search("{:03}Solution".format(numQ))
        moveToStart()
        highlightAbove()
        highlightRight()
        copy()
        swapWindows()
        if(index == finalSectionQ):
            adjustFinalPage()
        if (index == 23 or index == 25):
            columnBreak()
        paste()
        if(index == 21 or index == 23):
            for i in range(15):
                enter()

        swapWindows()
        if index < maxNumQ:
            search(str(index + 1))
            moveToStart()
            highlightAbove()
            highlightRight()
            delete()
    if convertPDF:
        swapWindows()
        convertToPDF(numBook)
    quitPages()


def readExamArray():
    startQ = None
    isStart = startQ == None
    f = open("prevQuestions.txt", "r")
    out = []
    index = 1
    for line in f.readlines():
        line = line.split(" ")
        numQ = int(line[0])
        if numQ == startQ:
            isStart = True

        if isStart:
            out.append((index, numQ, int(line[1]), int(line[2])))
        index += 1
    return out


def getExamArray():
    books = [1, 2, 3, 4, 5, 6]

    repeat = 4
    startBook = 1
    examStart = 1
    numQ = 59

    out = []
    index = 1
    for numBook in books:
        if numBook < startBook:
            continue

        examCount = len(lessons[numBook - 1])
        for numExam in range(1 if numBook > startBook else examStart, 1 + examCount):
            for i in range(repeat):
                out.append((index, numQ, numBook, numExam))
                numQ += 1
                index += 1
    return out


def getSpecificExam():
    numBook = 7
    numExam = 1
    numQ = 100
    return [(1, numQ, numBook, numExam)]


if __name__ == '__main__':
    convertPDF = True
    if pressNextMode:
        print("Press 'Enter' to go to next action")
    nums = getInputLines()
    # examArray = getExamArray()
    examArray = getSpecificExam()
    countDown()
    startTime = time()

    try:
        for (index, numQ, numBook, numExam) in examArray:
            print(str(index) + ". Starting Book:",
                  numBook, "Exam:", numExam, "v:", numQ)
            createFiles(numBook, numExam, numQ)
            setupFirstPage(numBook, numExam, numQ)
            if convertPDF:
                clearPDF(numBook, numExam, numQ)
            processFiles(nums[numQ - 1], numBook, numExam, convertPDF)
            openLectureFiles(numBook, numExam, numQ)
            processLectureFiles(numBook, numExam, nums[numQ - 1], convertPDF)

    except Exception as error:
        print("Terminate with Error:", error)
        print("Stack:", traceback.format_exc())

    print("Done:", round((time() - startTime) / 60, 2), "min")
