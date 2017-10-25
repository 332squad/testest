import sys
import subprocess
from time import sleep
import vk

if __name__ == "__main__":
    login = sys.argv[1]
    password = sys.argv[2]
    appId = 5483596
    session = vk.AuthSession(appId, login, password, scope="messages")
    sleep(0.34)
    vk_api = vk.API(session)
    numOfDialogs = vk_api.messages.getDialogs(count=0)[0]
    numOfReqs = 1 + numOfDialogs//200
    print("numOfDialogs: " + str(numOfDialogs))
    sleep(0.34)
    for x in range(0, numOfReqs):
        print('IN_GLOBAL: ' + str((x*20000)//numOfDialogs) + '%')
        res = vk_api.messages.getDialogs(count=200, offset=x*200)
        res.pop(0)
        for d in res:
            if 'chat_id' in d:
                subprocess.call(["python", "getDialogJSONFile.py", login, password, str(d.get('chat_id')), "0"], shell=True)
            else:
                subprocess.call(["python", "getDialogJSONFile.py", login, password, str(d.get('uid')), "1"], shell=True)
            sleep(0.34)
    print('WELL DONE!')