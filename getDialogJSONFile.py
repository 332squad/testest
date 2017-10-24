import sys
import json
from time import sleep
import vk

if __name__ == "__main__":
    login = ""
    password = ""
    dialog = 89 + 2000000000
    appId = 5483596
    if len (sys.argv) == 5 and int(sys.argv[4]) == 1:
        login = sys.argv[1]
        password = sys.argv[2]
        dialog = int(sys.argv[3])
        print("")
    elif len (sys.argv) == 5 and int(sys.argv[4]) == 0:
        login = sys.argv[1]
        password = sys.argv[2]
        dialog = int(sys.argv)+2000000000
        print("")
    else:
        print("недостаточно параметров")
        exit(-1)
        print("")
    session = vk.AuthSession(appId, login, password, scope="messages")
    vk_api = vk.API(session)
    res = vk_api.messages.getHistory(user_id = dialog, count = 0)
    numOfMessages = res[0]
    numOfIterations = (numOfMessages // 200) + 1
    sleep(0.34)
    messages = []
    for x in range(0, numOfIterations):
        messages += vk_api.messages.getHistory(user_id=dialog, count=200, offset=(x*200))
        print(str(100*x*200//numOfMessages) + '%')
        sleep(0.34)
    print('100%')
    f = open('messages.txt', 'w')
    for el in messages:
        if el != numOfMessages:
            neededEl = {"text" : el.get('body'), "id" : el.get('from_id')}
            f.write(json.dumps(neededEl)+'\n')