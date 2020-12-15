##################
## dependencies ##
##################
# pip install requests
# pip install playsound
##################

import requests
import time
from datetime import datetime
import urllib3
from playsound import playsound

urllib3.disable_warnings()
wavFile_status200 = "servers back online speech.wav"
wavFile_status500 = "error500.wav"
wavFile_status408 = "error408.wav"

wasOnline = [ True, True ]
wasOffline = [ False, False ]

def printTime(text, tag):
    print(datetime.now(), " [", tag, "] ", text)


def test_server_response(url, tag, index):
    global wasOnline
    global wasOffline

    try:
        r = requests.get(url, verify=False)
        printTime("status: " + str(r.status_code), tag)
        if r.status_code == 500:
            wasOffline[index] = True
            if wasOnline[index]:
                playsound(wavFile_status500)
                wasOnline[index] = False
        else:
            wasOnline[index] = True
            if wasOffline[index]:
                playsound(wavFile_status200)
                wasOffline[index] = False
        pass
    except requests.RequestException:
        printTime("timeout", tag)
        wasOffline[index] = True
        if wasOnline[index]:
            playsound(wavFile_status408)
            wasOnline[index] = False
        pass


while True:
    test_server_response('https://DOMAIN_ME', "PRODUCTION", 0)
    test_server_response('https://DOMAIN_ME', "TESTING", 1)
    time.sleep(10)
