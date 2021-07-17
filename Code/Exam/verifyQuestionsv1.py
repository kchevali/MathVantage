from selectQuestionsv2 import *


def run(startQ, total):
    fails = 0
    for index in range(startQ, total + 1):  # [1,125]
        if not search(str(index) + ". ", terminateOnFail=False):
            print("Failed: {} Regular".format(index))
            fails += 1
        if not search("{:03}Solution".format(index), terminateOnFail=False):
            print("Failed: {} Solution".format(index))
            fails += 1
    return fails


if __name__ == '__main__':
    print("Running Verify. Have the template (~125Q) open and ready.")
    # Verified Book 7 Exam 2
    startQ = 1
    total = 125  # Book 5 Exam 2 -> 115Q
    countDown()
    fails = run(startQ, total)
    print("Terminated with {} fails.".format(fails))
