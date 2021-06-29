import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0
for quesntionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s='%(quesntionNumber,num1,num2)

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1*num2)],
        blockRegexes=[('.*','Incorrect!')],
        timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of Time')
    except pyip.RetryLimitException:
        print('Out of tries')
    else:
        print('Correct')
        correctAnswers +=1

    time.sleep(1)
    print('Score: %s/%s'%(correctAnswers,numberOfQuestions))